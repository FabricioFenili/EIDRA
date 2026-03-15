from __future__ import annotations
import json
from pathlib import Path

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class PublishArtifactRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_publish_artifacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    instance_name TEXT NOT NULL,
                    target_name TEXT NOT NULL,
                    artifact_path TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def record(self, instance_name: str, target_name: str, artifact_path: str, metadata: dict):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_publish_artifacts(instance_name, target_name, artifact_path, metadata_json)
                VALUES (?, ?, ?, ?)
                ''',
                (instance_name, target_name, artifact_path, json.dumps(metadata)),
            )
            conn.commit()

    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT id, instance_name, target_name, artifact_path, metadata_json, created_at FROM control_publish_artifacts ORDER BY id DESC"
            ).fetchall()
        return [dict(r) for r in rows]
