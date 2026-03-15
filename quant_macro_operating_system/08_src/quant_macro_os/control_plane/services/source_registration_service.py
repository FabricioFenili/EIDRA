from __future__ import annotations

from quant_macro_os.control_plane.api.control_api import ControlAPI

class SourceRegistrationService:
    def __init__(self, api: ControlAPI):
        self.api = api

    def register_fake_source_e2e(
        self,
        source_name: str,
        source_type: str,
        source_config: dict,
        pipeline_name: str,
        steps: list[str],
        instance_name: str,
        data_family: str,
        canonical_contract_name: str,
        schedule_policy_name: str,
        publish_target_name: str,
        join_key_policy_name: str,
    ) -> dict:
        self.api.save_source(source_name, source_type, source_config)
        self.api.save_pipeline(pipeline_name, source_name, steps)
        self.api.save_source_instance(
            instance_name,
            source_template_name=source_name,
            source_name=source_name,
            data_family=data_family,
            canonical_contract_name=canonical_contract_name,
            schedule_policy_name=schedule_policy_name,
            publish_target_name=publish_target_name,
            join_key_policy_name=join_key_policy_name,
            pipeline_name=pipeline_name,
            is_enabled=True,
            metadata={"mode": "fake_registration"},
        )
        return {"status": "ok", "source_name": source_name, "instance_name": instance_name}
