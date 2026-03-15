from __future__ import annotations
import json
from pathlib import Path

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class PublishTargetRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_publish_targets (
                    target_name TEXT PRIMARY KEY,
                    layer TEXT NOT NULL,
                    model_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def upsert(self, target_name, layer, model_name, description, metadata=None):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_publish_targets(target_name, layer, model_name, description, metadata_json, updated_at)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(target_name) DO UPDATE SET
                    layer = excluded.layer,
                    model_name = excluded.model_name,
                    description = excluded.description,
                    metadata_json = excluded.metadata_json,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (target_name, layer, model_name, description, json.dumps(metadata or {})),
            )
            conn.commit()

    def get(self, target_name):
        with connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT target_name, layer, model_name, description, metadata_json, updated_at FROM control_publish_targets WHERE target_name = ?",
                (target_name,),
            ).fetchone()
        return dict(row) if row else {}

    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute("SELECT target_name, layer, model_name, description, metadata_json, updated_at FROM control_publish_targets ORDER BY target_name").fetchall()
        return [dict(r) for r in rows]
