from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path


class ParameterRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_parameters (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def set(self, key: str, value: Any) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_parameters(key, value, updated_at)
                VALUES(?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(key) DO UPDATE SET
                    value = excluded.value,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (key, str(value)),
            )
            conn.commit()

    def get(self, key: str, default: Any = None) -> Any:
        with connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT value FROM control_parameters WHERE key = ?",
                (key,),
            ).fetchone()
        return row["value"] if row else default

    def all(self) -> Dict[str, Any]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT key, value FROM control_parameters ORDER BY key"
            ).fetchall()
        return {row["key"]: row["value"] for row in rows}
