from __future__ import annotations
import json
from pathlib import Path
from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class ContractRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()
    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS control_contracts (
                    contract_name TEXT PRIMARY KEY,
                    schema_version TEXT NOT NULL,
                    normalized_contract_json TEXT NOT NULL,
                    quality_checks_json TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    def upsert(self, contract_name, schema_version, normalized_contract, quality_checks, metadata=None):
        with connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO control_contracts(contract_name, schema_version, normalized_contract_json, quality_checks_json, metadata_json, updated_at)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(contract_name) DO UPDATE SET
                    schema_version = excluded.schema_version,
                    normalized_contract_json = excluded.normalized_contract_json,
                    quality_checks_json = excluded.quality_checks_json,
                    metadata_json = excluded.metadata_json,
                    updated_at = CURRENT_TIMESTAMP
            ''', (contract_name, schema_version, json.dumps(normalized_contract), json.dumps(quality_checks), json.dumps(metadata or {})))
            conn.commit()
    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute("SELECT contract_name, schema_version, normalized_contract_json, quality_checks_json, metadata_json, updated_at FROM control_contracts ORDER BY contract_name").fetchall()
        return [dict(r) for r in rows]
