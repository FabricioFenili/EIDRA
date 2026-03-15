from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path


class PatchRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_patches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    target_file TEXT NOT NULL,
                    content TEXT NOT NULL,
                    status TEXT NOT NULL,
                    approver TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    metadata_json TEXT
                )
                '''
            )
            conn.commit()

    def create(self, target_file: str, content: str, metadata: Dict[str, object] | None = None) -> int:
        with connect(self.db_path) as conn:
            cursor = conn.execute(
                '''
                INSERT INTO control_patches(target_file, content, status, metadata_json)
                VALUES (?, ?, 'staged', ?)
                ''',
                (target_file, content, json.dumps(metadata or {})),
            )
            conn.commit()
            return int(cursor.lastrowid)

    def approve(self, patch_id: int, approver: str) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                UPDATE control_patches
                SET status = 'approved',
                    approver = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
                ''',
                (approver, patch_id),
            )
            conn.commit()

    def mark_applied(self, patch_id: int) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                UPDATE control_patches
                SET status = 'applied',
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
                ''',
                (patch_id,),
            )
            conn.commit()

    def get(self, patch_id: int) -> Dict[str, object]:
        with connect(self.db_path) as conn:
            row = conn.execute(
                '''
                SELECT id, target_file, content, status, approver, created_at, updated_at, metadata_json
                FROM control_patches
                WHERE id = ?
                ''',
                (patch_id,),
            ).fetchone()
        return dict(row) if row else {}

    def list_all(self) -> List[Dict[str, object]]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                '''
                SELECT id, target_file, status, approver, created_at, updated_at, metadata_json
                FROM control_patches
                ORDER BY id DESC
                '''
            ).fetchall()
        return [dict(row) for row in rows]
