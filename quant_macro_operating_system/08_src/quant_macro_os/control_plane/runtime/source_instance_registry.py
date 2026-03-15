from __future__ import annotations
import json
from pathlib import Path

from quant_macro_os.control_plane.services.db import connect
from quant_macro_os.control_plane.services.paths import get_db_path

class SourceInstanceRegistry:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None):
        self.db_path = db_path or get_db_path(repo_root)
        self._init_db()

    def _init_db(self):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS control_source_instances (
                    instance_name TEXT PRIMARY KEY,
                    source_template_name TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    data_family TEXT NOT NULL,
                    canonical_contract_name TEXT NOT NULL,
                    schedule_policy_name TEXT NOT NULL,
                    publish_target_name TEXT NOT NULL,
                    join_key_policy_name TEXT NOT NULL,
                    pipeline_name TEXT NOT NULL,
                    is_enabled INTEGER NOT NULL,
                    metadata_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()

    def upsert(
        self,
        instance_name: str,
        source_template_name: str,
        source_name: str,
        data_family: str,
        canonical_contract_name: str,
        schedule_policy_name: str,
        publish_target_name: str,
        join_key_policy_name: str,
        pipeline_name: str,
        is_enabled: bool,
        metadata: dict | None = None,
    ):
        with connect(self.db_path) as conn:
            conn.execute(
                '''
                INSERT INTO control_source_instances(
                    instance_name, source_template_name, source_name, data_family, canonical_contract_name,
                    schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name,
                    is_enabled, metadata_json, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(instance_name) DO UPDATE SET
                    source_template_name = excluded.source_template_name,
                    source_name = excluded.source_name,
                    data_family = excluded.data_family,
                    canonical_contract_name = excluded.canonical_contract_name,
                    schedule_policy_name = excluded.schedule_policy_name,
                    publish_target_name = excluded.publish_target_name,
                    join_key_policy_name = excluded.join_key_policy_name,
                    pipeline_name = excluded.pipeline_name,
                    is_enabled = excluded.is_enabled,
                    metadata_json = excluded.metadata_json,
                    updated_at = CURRENT_TIMESTAMP
                ''',
                (
                    instance_name, source_template_name, source_name, data_family, canonical_contract_name,
                    schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name,
                    1 if is_enabled else 0, json.dumps(metadata or {}),
                ),
            )
            conn.commit()

    def get(self, instance_name: str):
        with connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT instance_name, source_template_name, source_name, data_family, canonical_contract_name, schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name, is_enabled, metadata_json, updated_at FROM control_source_instances WHERE instance_name = ?",
                (instance_name,),
            ).fetchone()
        return dict(row) if row else {}

    def list_all(self):
        with connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT instance_name, source_template_name, source_name, data_family, canonical_contract_name, schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name, is_enabled, metadata_json, updated_at FROM control_source_instances ORDER BY instance_name"
            ).fetchall()
        return [dict(r) for r in rows]
