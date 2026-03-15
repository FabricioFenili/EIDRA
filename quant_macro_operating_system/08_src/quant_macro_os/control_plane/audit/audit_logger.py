from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path


class AuditLogger:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_audit_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    action TEXT NOT NULL,
                    detail TEXT NOT NULL,
                    target_file TEXT,
                    status TEXT,
                    metadata_json TEXT
                )
                '''
            )
            conn.commit()

    def record(
        self,
        action: str,
        detail: str,
        target_file: str | None = None,
        status: str | None = None,
        metadata: Dict[str, object] | None = None,
    ) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_audit_events(action, detail, target_file, status, metadata_json)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (action, detail, target_file, status, json.dumps(metadata or {})),
            )
            conn.commit()

    def all(self) -> List[Dict[str, str]]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                '''
                SELECT timestamp, action, detail, target_file, status, metadata_json
                FROM control_audit_events
                ORDER BY id DESC
                '''
            ).fetchall()
        return [dict(row) for row in rows]
