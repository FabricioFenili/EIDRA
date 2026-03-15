from __future__ import annotations
import json
from pathlib import Path
from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class DataFamilyRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()
    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS control_data_families (
                    family_name TEXT PRIMARY KEY,
                    description TEXT NOT NULL,
                    canonical_contract TEXT NOT NULL,
                    grain TEXT NOT NULL,
                    owner_vp TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    def upsert(self, family_name, description, canonical_contract, grain, owner_vp, metadata=None):
        with connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO control_data_families(family_name, description, canonical_contract, grain, owner_vp, metadata_json, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(family_name) DO UPDATE SET
                    description = excluded.description,
                    canonical_contract = excluded.canonical_contract,
                    grain = excluded.grain,
                    owner_vp = excluded.owner_vp,
                    metadata_json = excluded.metadata_json,
                    updated_at = CURRENT_TIMESTAMP
            ''', (family_name, description, canonical_contract, grain, owner_vp, json.dumps(metadata or {})))
            conn.commit()
    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute("SELECT family_name, description, canonical_contract, grain, owner_vp, metadata_json, updated_at FROM control_data_families ORDER BY family_name").fetchall()
        return [dict(r) for r in rows]
