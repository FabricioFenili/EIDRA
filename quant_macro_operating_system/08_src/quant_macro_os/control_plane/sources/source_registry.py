from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class SourceRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_sources (
                    name TEXT PRIMARY KEY,
                    source_type TEXT NOT NULL,
                    config_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def upsert(self, name: str, source_type: str, config: Dict[str, object]) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_sources(name, source_type, config_json, updated_at)
                VALUES(?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(name) DO UPDATE SET
                    source_type = excluded.source_type,
                    config_json = excluded.config_json,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (name, source_type, json.dumps(config)),
            )
            conn.commit()

    def get(self, name: str) -> Dict[str, object]:
        with connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT name, source_type, config_json, updated_at FROM control_sources WHERE name = ?",
                (name,),
            ).fetchone()
        return dict(row) if row else {}

    def list_all(self) -> List[Dict[str, str]]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT name, source_type, config_json, updated_at FROM control_sources ORDER BY name"
            ).fetchall()
        return [dict(row) for row in rows]


    def delete(self, name: str) -> None:
        with connect(self.db_path) as conn:
            conn.execute("DELETE FROM control_sources WHERE name = ?", (name,))
            conn.commit()
