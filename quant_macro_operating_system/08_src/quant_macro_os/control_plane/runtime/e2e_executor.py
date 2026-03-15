from __future__ import annotations
import json

from quant_macro_os.control_plane.runtime.source_instance_registry import SourceInstanceRegistry
from quant_macro_os.control_plane.runtime.runtime_scheduler import RuntimeScheduler
from quant_macro_os.control_plane.pipeline.pipeline_controller import PipelineController

class E2EExecutor:
    def __init__(self, db_path=None, repo_root=None, workdir=None):
        self.instances = SourceInstanceRegistry(db_path=db_path, repo_root=repo_root)
        self.scheduler = RuntimeScheduler(db_path=db_path, repo_root=repo_root)
        self.pipeline = PipelineController(db_path=db_path, repo_root=repo_root, workdir=workdir)

    def run_source_instance(self, instance_name: str, year: int, month: int, day: int):
        instance = self.instances.get(instance_name)
        if not instance:
            return {"status": "source_instance_not_found", "instance_name": instance_name}
        plan = self.scheduler.plan_for_date(year, month, day)
        planned_names = {item["instance_name"] for item in plan}
        if instance_name not in planned_names:
            return {"status": "source_instance_not_eligible", "instance_name": instance_name, "planned_instances": sorted(planned_names)}

        metadata = json.loads(instance["metadata_json"])
        runtime_params = {
            "instance_name": instance["instance_name"],
            "source_name_override": instance["source_name"],
            "data_family": instance["data_family"],
            "canonical_contract_name": instance["canonical_contract_name"],
            "publish_target_name": instance["publish_target_name"],
            "join_key_policy_name": instance["join_key_policy_name"],
            "execution_date": f"{year:04d}-{month:02d}-{day:02d}",
            "instance_metadata": metadata,
        }
        result = self.pipeline.run_pipeline(instance["pipeline_name"], runtime_params)
        result["instance_name"] = instance_name
        return result
