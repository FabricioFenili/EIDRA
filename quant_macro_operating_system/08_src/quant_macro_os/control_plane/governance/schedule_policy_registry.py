from __future__ import annotations
import json
from pathlib import Path

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class SchedulePolicyRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_schedule_policies (
                    policy_name TEXT PRIMARY KEY,
                    update_frequency TEXT NOT NULL,
                    execution_policy TEXT NOT NULL,
                    freshness_sla TEXT NOT NULL,
                    timezone TEXT NOT NULL,
                    first_eligible_time TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def upsert(self, policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata=None):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_schedule_policies(policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata_json, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(policy_name) DO UPDATE SET
                    update_frequency = excluded.update_frequency,
                    execution_policy = excluded.execution_policy,
                    freshness_sla = excluded.freshness_sla,
                    timezone = excluded.timezone,
                    first_eligible_time = excluded.first_eligible_time,
                    metadata_json = excluded.metadata_json,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, json.dumps(metadata or {})),
            )
            conn.commit()

    def get(self, policy_name):
        with connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata_json, updated_at FROM control_schedule_policies WHERE policy_name = ?",
                (policy_name,),
            ).fetchone()
        return dict(row) if row else {}

    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute("SELECT policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata_json, updated_at FROM control_schedule_policies ORDER BY policy_name").fetchall()
        return [dict(r) for r in rows]
