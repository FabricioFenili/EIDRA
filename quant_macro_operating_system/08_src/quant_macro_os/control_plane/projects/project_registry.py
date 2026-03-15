from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path


class ProjectRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_projects (
                    name TEXT PRIMARY KEY,
                    description TEXT NOT NULL,
                    owner TEXT NOT NULL,
                    status TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def upsert(self, name: str, description: str, owner: str, status: str) -> None:
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_projects(name, description, owner, status, updated_at)
                VALUES(?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(name) DO UPDATE SET
                    description = excluded.description,
                    owner = excluded.owner,
                    status = excluded.status,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (name, description, owner, status),
            )
            conn.commit()

    def list_all(self) -> List[Dict[str, str]]:
        with connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT name, description, owner, status, updated_at FROM control_projects ORDER BY name"
            ).fetchall()
        return [dict(row) for row in rows]


    def delete(self, name: str) -> None:
        with connect(self.db_path) as conn:
            conn.execute("DELETE FROM control_projects WHERE name = ?", (name,))
            conn.commit()
