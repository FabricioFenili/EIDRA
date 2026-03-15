from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path


class PipelineRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_pipelines (
                    name TEXT PRIMARY KEY,
                    source_name TEXT NOT NULL,
                    steps_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_pipeline_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pipeline_name TEXT NOT NULL,
                    runtime_params_json TEXT NOT NULL,
                    status TEXT NOT NULL,
                    result_json TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def upsert(self, name: str, source_name: str, steps: List[str]) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_pipelines(name, source_name, steps_json, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(name) DO UPDATE SET
                    source_name = excluded.source_name,
                    steps_json = excluded.steps_json,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (name, source_name, json.dumps(steps)),
            )
            conn.commit()

    def list_all(self) -> List[Dict[str, object]]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT name, source_name, steps_json, updated_at FROM control_pipelines ORDER BY name"
            ).fetchall()
        return [dict(row) for row in rows]

    def get(self, name: str) -> Dict[str, object]:
        with connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT name, source_name, steps_json, updated_at FROM control_pipelines WHERE name = ?",
                (name,),
            ).fetchone()
        return dict(row) if row else {}

    def record_run(self, pipeline_name: str, runtime_params: Dict[str, object], status: str, result: Dict[str, object]) -> int:
        with connect(self.db_path) as conn:
            cursor = conn.execute(
                '''
                INSERT INTO control_pipeline_runs(pipeline_name, runtime_params_json, status, result_json)
                VALUES (?, ?, ?, ?)
                ''',
                (pipeline_name, json.dumps(runtime_params), status, json.dumps(result)),
            )
            conn.commit()
            return int(cursor.lastrowid)

    def list_runs(self) -> List[Dict[str, object]]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                '''
                SELECT id, pipeline_name, runtime_params_json, status, result_json, created_at
                FROM control_pipeline_runs
                ORDER BY id DESC
                '''
            ).fetchall()
        return [dict(row) for row in rows]
