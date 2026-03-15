from __future__ import annotations
import json
from pathlib import Path

from quant_macro_os.bootstrap.system_bootstrap_pipeline import bootstrap
from quant_macro_os.control_plane.pipeline.pipeline_registry import PipelineRegistry
from quant_macro_os.control_plane.pipeline.step_executor import StepExecutor
from quant_macro_os.control_plane.sources.source_registry import SourceRegistry
from quant_macro_os.control_plane.sources.source_executor import SourceExecutor
from quant_macro_os.control_plane.governance.publish_target_registry import PublishTargetRegistry
from quant_macro_os.control_plane.publish.publish_artifact_registry import PublishArtifactRegistry
from quant_macro_os.control_plane.publish.publish_materializer import PublishMaterializer

class PipelineController:
    def __init__(self, db_path: Path | None = None, repo_root: Path | None = None, workdir: Path | None = None):
        self.registry = PipelineRegistry(db_path=db_path, repo_root=repo_root)
        self.sources = SourceRegistry(db_path=db_path, repo_root=repo_root)
        self.source_executor = SourceExecutor()
        self.steps = StepExecutor()
        self.publish_targets = PublishTargetRegistry(db_path=db_path, repo_root=repo_root)
        self.publish_artifacts = PublishArtifactRegistry(db_path=db_path, repo_root=repo_root)
        self.materializer = PublishMaterializer(workdir=workdir)

    def run_bootstrap(self, db_path: Path) -> Path:
        return bootstrap(db_path)

    def save_pipeline(self, name: str, source_name: str, steps: list[str]) -> None:
        self.registry.upsert(name, source_name, steps)

    def list_pipelines(self):
        return self.registry.list_all()

    def list_runs(self):
        return self.registry.list_runs()

    def list_publish_artifacts(self):
        return self.publish_artifacts.list_all()

    def run_pipeline(self, name: str, runtime_params: dict | None = None) -> dict:
        runtime_params = runtime_params or {}
        pipeline = self.registry.get(name)
        if not pipeline:
            result = {"pipeline": name, "status": "pipeline_not_found", "steps_executed": []}
            self.registry.record_run(name, runtime_params, "fail", result)
            return result

        effective_source_name = runtime_params.get("source_name_override") or pipeline["source_name"]
        source_record = self.sources.get(effective_source_name)
        if source_record:
            source_payload = self.source_executor.execute(source_record)
        else:
            source_payload = {"status": "source_not_found", "source_name": effective_source_name}

        steps = json.loads(pipeline["steps_json"])
        step_result = self.steps.execute(source_payload, steps, runtime_params)

        publish_target_name = runtime_params.get("publish_target_name", "")
        instance_name = runtime_params.get("instance_name", effective_source_name)
        published_path = None
        if step_result["published"] and publish_target_name:
            target = self.publish_targets.get(publish_target_name)
            if target:
                payload = {
                    "instance_name": instance_name,
                    "pipeline_name": name,
                    "publish_target_name": publish_target_name,
                    "layer": target["layer"],
                    "model_name": target["model_name"],
                    "data_family": runtime_params.get("data_family"),
                    "canonical_contract_name": runtime_params.get("canonical_contract_name"),
                    "execution_date": runtime_params.get("execution_date"),
                    "source_payload": source_payload,
                    "steps_executed": step_result["steps_executed"],
                }
                artifact = self.materializer.materialize(target["model_name"], instance_name, payload)
                published_path = str(artifact)
                self.publish_artifacts.record(instance_name, publish_target_name, published_path, payload)

        result = {
            "pipeline": name,
            "source_name": effective_source_name,
            "status": step_result["status"],
            "steps_executed": step_result["steps_executed"],
            "unsupported_steps": step_result["unsupported_steps"],
            "published": step_result["published"] and bool(published_path),
            "published_path": published_path,
            "runtime_params": runtime_params,
        }
        self.registry.record_run(name, runtime_params, result["status"], result)
        return result
