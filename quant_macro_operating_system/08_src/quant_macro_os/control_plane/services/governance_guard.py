from __future__ import annotations

ALLOWED_SOURCE_TYPES = {"manual", "api", "file", "database", "html", "object_storage"}
ALLOWED_PIPELINE_STEPS = {"source", "ingest", "normalize", "validate", "publish", "feature", "curate"}

class GovernanceGuard:
    def validate_source(self, name: str, source_type: str, config: dict) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("source_name_required")
        if source_type not in ALLOWED_SOURCE_TYPES:
            raise ValueError(f"invalid_source_type:{source_type}")
        if not isinstance(config, dict):
            raise ValueError("source_config_must_be_dict")

    def validate_pipeline(self, name: str, source_name: str, steps: list[str], source_names: list[str]) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("pipeline_name_required")
        if source_name not in set(source_names):
            raise ValueError(f"pipeline_source_not_registered:{source_name}")
        if not isinstance(steps, list) or not steps:
            raise ValueError("pipeline_steps_required")
        if steps[0] != "source":
            raise ValueError("pipeline_must_start_with_source")
        if "publish" not in steps:
            raise ValueError("pipeline_must_include_publish")
        invalid = [step for step in steps if step not in ALLOWED_PIPELINE_STEPS]
        if invalid:
            raise ValueError(f"invalid_pipeline_steps:{','.join(invalid)}")

    def validate_source_instance(
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
        source_names: list[str],
        data_families: list[str],
        contracts: list[str],
        schedules: list[str],
        publish_targets: list[str],
        join_key_policies: list[str],
        pipeline_source_map: dict[str, str],
    ) -> None:
        required_pairs = {
            "instance_name": instance_name,
            "source_template_name": source_template_name,
            "source_name": source_name,
            "data_family": data_family,
            "canonical_contract_name": canonical_contract_name,
            "schedule_policy_name": schedule_policy_name,
            "publish_target_name": publish_target_name,
            "join_key_policy_name": join_key_policy_name,
            "pipeline_name": pipeline_name,
        }
        for field, value in required_pairs.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field}_required")

        if source_name not in set(source_names):
            raise ValueError(f"source_not_registered:{source_name}")
        if source_template_name not in set(source_names):
            raise ValueError(f"source_template_not_registered:{source_template_name}")
        if data_family not in set(data_families):
            raise ValueError(f"unknown_data_family:{data_family}")
        if canonical_contract_name not in set(contracts):
            raise ValueError(f"unknown_contract:{canonical_contract_name}")
        if schedule_policy_name not in set(schedules):
            raise ValueError(f"unknown_schedule_policy:{schedule_policy_name}")
        if publish_target_name not in set(publish_targets):
            raise ValueError(f"unknown_publish_target:{publish_target_name}")
        if join_key_policy_name not in set(join_key_policies):
            raise ValueError(f"unknown_join_key_policy:{join_key_policy_name}")
        if pipeline_name not in pipeline_source_map:
            raise ValueError(f"unknown_pipeline:{pipeline_name}")

        pipeline_source_name = pipeline_source_map[pipeline_name]
        if pipeline_source_name != source_name:
            raise ValueError(
                f"pipeline_source_mismatch:pipeline={pipeline_name}:expected_source={pipeline_source_name}:received_source={source_name}"
            )
