from __future__ import annotations
import json
from pathlib import Path
from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class JoinKeyPolicyRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()
    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS control_join_key_policies (
                    policy_name TEXT PRIMARY KEY,
                    data_family TEXT NOT NULL,
                    key_columns_json TEXT NOT NULL,
                    time_key TEXT NOT NULL,
                    alignment_policy TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    def upsert(self, policy_name, data_family, key_columns, time_key, alignment_policy, metadata=None):
        with connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO control_join_key_policies(policy_name, data_family, key_columns_json, time_key, alignment_policy, metadata_json, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(policy_name) DO UPDATE SET
                    data_family = excluded.data_family,
                    key_columns_json = excluded.key_columns_json,
                    time_key = excluded.time_key,
                    alignment_policy = excluded.alignment_policy,
                    metadata_json = excluded.metadata_json,
                    updated_at = CURRENT_TIMESTAMP
            ''', (policy_name, data_family, json.dumps(key_columns), time_key, alignment_policy, json.dumps(metadata or {})))
            conn.commit()
    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute("SELECT policy_name, data_family, key_columns_json, time_key, alignment_policy, metadata_json, updated_at FROM control_join_key_policies ORDER BY policy_name").fetchall()
        return [dict(r) for r in rows]
