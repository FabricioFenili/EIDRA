from __future__ import annotations
from pathlib import Path

from quant_macro_os.control_plane.audit.audit_logger import AuditLogger
from quant_macro_os.control_plane.config.parameter_registry import ParameterRegistry
from quant_macro_os.control_plane.patch_manager.patch_applier import PatchApplier
from quant_macro_os.control_plane.patch_manager.patch_generator import PatchGenerator
from quant_macro_os.control_plane.patch_manager.patch_registry import PatchRegistry
from quant_macro_os.control_plane.patch_manager.patch_validator import PatchValidator
from quant_macro_os.control_plane.pipeline.pipeline_controller import PipelineController
from quant_macro_os.control_plane.projects.project_registry import ProjectRegistry
from quant_macro_os.control_plane.services.diff_service import DiffService
from quant_macro_os.control_plane.governance.data_family_registry import DataFamilyRegistry
from quant_macro_os.control_plane.governance.contract_registry import ContractRegistry
from quant_macro_os.control_plane.governance.schedule_policy_registry import SchedulePolicyRegistry
from quant_macro_os.control_plane.governance.publish_target_registry import PublishTargetRegistry
from quant_macro_os.control_plane.governance.join_key_policy_registry import JoinKeyPolicyRegistry
from quant_macro_os.control_plane.services.execution_eligibility_engine import ExecutionEligibilityEngine
from quant_macro_os.control_plane.services.git_service import GitService
from quant_macro_os.control_plane.services.repo_browser import RepoBrowser
from quant_macro_os.control_plane.services.test_runner import TestRunner
from quant_macro_os.control_plane.services.governance_guard import GovernanceGuard
from quant_macro_os.control_plane.runtime.source_instance_registry import SourceInstanceRegistry
from quant_macro_os.control_plane.runtime.runtime_scheduler import RuntimeScheduler
from quant_macro_os.control_plane.runtime.e2e_executor import E2EExecutor
from quant_macro_os.control_plane.sources.source_registry import SourceRegistry
from quant_macro_os.control_plane.sources.source_catalog_service import SourceCatalogService
from quant_macro_os.control_plane.sources.source_templates import SOURCE_TEMPLATES
from quant_macro_os.control_plane.pipeline.pipeline_presets import PIPELINE_PRESETS
from quant_macro_os.control_plane.services.artifact_factory import ArtifactFactory

class ControlAPI:
    def __init__(self, repo_root: Path, db_path: Path | None = None, workdir: Path | None = None):
        self.repo_root = repo_root.resolve()
        self.projects = ProjectRegistry(db_path=db_path, repo_root=self.repo_root)
        self.sources = SourceRegistry(db_path=db_path, repo_root=self.repo_root)
        self.parameters = ParameterRegistry(db_path=db_path, repo_root=self.repo_root)
        self.audit = AuditLogger(db_path=db_path, repo_root=self.repo_root)
        self.generator = PatchGenerator()
        self.patch_registry = PatchRegistry(db_path=db_path, repo_root=self.repo_root)
        self.validator = PatchValidator()
        self.applier = PatchApplier(workdir=workdir)
        self.pipeline = PipelineController(db_path=db_path, repo_root=self.repo_root, workdir=workdir)
        self.browser = RepoBrowser(self.repo_root)
        self.diff_service = DiffService()
        self.tests = TestRunner(self.repo_root)
        self.git = GitService(self.repo_root)
        self.guard = GovernanceGuard()
        self.data_families = DataFamilyRegistry(db_path=db_path, repo_root=self.repo_root)
        self.contracts = ContractRegistry(db_path=db_path, repo_root=self.repo_root)
        self.schedule_policies = SchedulePolicyRegistry(db_path=db_path, repo_root=self.repo_root)
        self.publish_targets = PublishTargetRegistry(db_path=db_path, repo_root=self.repo_root)
        self.join_key_policies = JoinKeyPolicyRegistry(db_path=db_path, repo_root=self.repo_root)
        self.eligibility = ExecutionEligibilityEngine()
        self.source_instances = SourceInstanceRegistry(db_path=db_path, repo_root=self.repo_root)
        self.runtime_scheduler = RuntimeScheduler(db_path=db_path, repo_root=self.repo_root)
        self.e2e = E2EExecutor(db_path=db_path, repo_root=self.repo_root, workdir=workdir)
        self.source_catalog = SourceCatalogService()
        self.artifacts = ArtifactFactory(self.repo_root)

    def save_project(self, name, description, owner, status):
        self.projects.upsert(name, description, owner, status)
        self.audit.record("save_project", name, status="ok")

    def list_projects(self):
        return self.projects.list_all()

    def save_source(self, name, source_type, config):
        self.guard.validate_source(name, source_type, config)
        self.sources.upsert(name, source_type, config)
        artifacts = self.artifacts.write_source(name, source_type, config)
        self.audit.record("save_source", name, status="ok", metadata={"source_type": source_type, "artifacts": artifacts})

    def list_sources(self):
        return self.sources.list_all()

    def set_parameter(self, key, value):
        self.parameters.set(key, value)
        self.audit.record("set_parameter", f"{key}={value}", status="ok")

    def get_parameters(self):
        return self.parameters.all()

    def save_pipeline(self, name, source_name, steps):
        source_names = [row["name"] for row in self.list_sources()]
        self.guard.validate_pipeline(name, source_name, steps, source_names)
        self.pipeline.save_pipeline(name, source_name, steps)
        artifacts = self.artifacts.write_pipeline(name, source_name, steps)
        self.audit.record("save_pipeline", name, status="ok", metadata={"source_name": source_name, "steps": steps, "artifacts": artifacts})

    def list_pipelines(self):
        return self.pipeline.list_pipelines()

    def list_pipeline_runs(self):
        return self.pipeline.list_runs()

    def list_publish_artifacts(self):
        return self.pipeline.list_publish_artifacts()

    def run_pipeline(self, name, runtime_params=None):
        result = self.pipeline.run_pipeline(name, runtime_params)
        self.audit.record("run_pipeline", name, status=result["status"], metadata=result)
        return result

    def list_files(self):
        return self.browser.list_files()

    def read_file(self, relative_path):
        return self.browser.read_file(relative_path)

    def preview_diff(self, target_file, content):
        diff = self.diff_service.diff_for_file(self.repo_root, target_file, content)
        self.audit.record("preview_diff", "preview_generated", target_file=target_file, status="ok")
        return diff

    def stage_patch(self, target_file, content):
        patch_id = self.patch_registry.create(target_file, content)
        self.audit.record("stage_patch", f"patch_id={patch_id}", target_file=target_file, status="ok")
        return patch_id

    def list_patches(self):
        return self.patch_registry.list_all()

    def approve_patch(self, patch_id, approver):
        self.patch_registry.approve(patch_id, approver)
        self.audit.record("approve_patch", f"patch_id={patch_id}", status="ok", metadata={"approver": approver})

    def validate_patch(self, target_file, content):
        result = self.validator.validate(target_file, content, self.repo_root)
        self.audit.record("validate_patch", result.reason, target_file=target_file, status="ok" if result.valid else "fail")
        return result.reason

    def apply_patch(self, patch_id):
        patch = self.patch_registry.get(patch_id)
        if not patch or patch.get("status") != "approved":
            raise ValueError("patch_not_approved")
        reason = self.validate_patch(patch["target_file"], patch["content"])
        if reason != "ok":
            raise ValueError(reason)
        tests_dir = self.repo_root / "09_tests"
        if tests_dir.exists() and any(tests_dir.rglob("test_*.py")):
            tests = self.run_tests()
            if not tests["ok"]:
                raise ValueError("tests_failed_before_apply")
        result = self.applier.apply(self.repo_root, patch["target_file"], patch["content"])
        self.patch_registry.mark_applied(patch_id)
        self.audit.record("apply_patch", result.backup_path, target_file=patch["target_file"], status="ok")
        return result.backup_path

    def rollback_patch(self, target_file):
        ok = self.applier.rollback(self.repo_root, target_file)
        self.audit.record("rollback_patch", "rollback_attempted", target_file=target_file, status="ok" if ok else "fail")
        return ok

    def run_tests(self):
        result = self.tests.run()
        self.audit.record("run_tests", "pytest_executed", status="ok" if result["ok"] else "fail")
        return result

    def get_audit_events(self):
        return self.audit.all()

    def git_status(self):
        return self.git.status()

    def get_source_templates(self):
        return SOURCE_TEMPLATES

    def get_source_catalog(self):
        return self.source_catalog.list_templates()

    def get_source_catalog_categories(self):
        return self.source_catalog.list_categories()

    def create_source_from_template(self, template_name, source_name=None):
        template = SOURCE_TEMPLATES[template_name]
        resolved_name = source_name or template_name
        self.save_source(resolved_name, template["source_type"], template["config"])
        return {"name": resolved_name, **template}

    def get_pipeline_presets(self):
        return PIPELINE_PRESETS

    def create_pipeline_from_preset(self, preset_name, pipeline_name=None):
        preset = PIPELINE_PRESETS[preset_name]
        resolved_name = pipeline_name or preset_name
        self.save_pipeline(resolved_name, preset["source_name"], preset["steps"])
        return {"name": resolved_name, **preset}

    def save_data_family(self, family_name, description, canonical_contract, grain, owner_vp, metadata=None):
        self.data_families.upsert(family_name, description, canonical_contract, grain, owner_vp, metadata or {})
        artifacts = self.artifacts.write_data_family(family_name, description, canonical_contract, grain, owner_vp, metadata or {})
        self.audit.record("save_data_family", family_name, status="ok", metadata={"artifacts": artifacts})

    def list_data_families(self):
        return self.data_families.list_all()

    def save_contract(self, contract_name, schema_version, normalized_contract, quality_checks, metadata=None):
        self.contracts.upsert(contract_name, schema_version, normalized_contract, quality_checks, metadata or {})
        artifacts = self.artifacts.write_contract(contract_name, schema_version, normalized_contract, quality_checks, metadata or {})
        self.audit.record("save_contract", contract_name, status="ok", metadata={"artifacts": artifacts})

    def list_contracts(self):
        return self.contracts.list_all()

    def save_schedule_policy(self, policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata=None):
        self.schedule_policies.upsert(policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata or {})
        artifacts = self.artifacts.write_schedule_policy(policy_name, update_frequency, execution_policy, freshness_sla, timezone, first_eligible_time, metadata or {})
        self.audit.record("save_schedule_policy", policy_name, status="ok", metadata={"artifacts": artifacts})

    def list_schedule_policies(self):
        return self.schedule_policies.list_all()

    def save_publish_target(self, target_name, layer, model_name, description, metadata=None):
        self.publish_targets.upsert(target_name, layer, model_name, description, metadata or {})
        artifacts = self.artifacts.write_publish_target(target_name, layer, model_name, description, metadata or {})
        self.audit.record("save_publish_target", target_name, status="ok", metadata={"artifacts": artifacts})

    def list_publish_targets(self):
        return self.publish_targets.list_all()

    def save_join_key_policy(self, policy_name, data_family, key_columns, time_key, alignment_policy, metadata=None):
        self.join_key_policies.upsert(policy_name, data_family, key_columns, time_key, alignment_policy, metadata or {})
        artifacts = self.artifacts.write_join_key_policy(policy_name, data_family, key_columns, time_key, alignment_policy, metadata or {})
        self.audit.record("save_join_key_policy", policy_name, status="ok", metadata={"artifacts": artifacts})

    def list_join_key_policies(self):
        return self.join_key_policies.list_all()

    def evaluate_schedule(self, update_frequency, year, month, day):
        from datetime import date
        return self.eligibility.should_run(update_frequency, date(year, month, day))

    def save_source_instance(self, instance_name, source_template_name, source_name, data_family, canonical_contract_name, schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name, is_enabled=True, metadata=None):
        source_names = [row["name"] for row in self.list_sources()]
        data_families = [row["family_name"] for row in self.list_data_families()]
        contracts = [row["contract_name"] for row in self.list_contracts()]
        schedules = [row["policy_name"] for row in self.list_schedule_policies()]
        publish_targets = [row["target_name"] for row in self.list_publish_targets()]
        join_key_policies = [row["policy_name"] for row in self.list_join_key_policies()]
        pipeline_source_map = {row["name"]: row["source_name"] for row in self.list_pipelines()}
        self.guard.validate_source_instance(
            instance_name=instance_name,
            source_template_name=source_template_name,
            source_name=source_name,
            data_family=data_family,
            canonical_contract_name=canonical_contract_name,
            schedule_policy_name=schedule_policy_name,
            publish_target_name=publish_target_name,
            join_key_policy_name=join_key_policy_name,
            pipeline_name=pipeline_name,
            source_names=source_names,
            data_families=data_families,
            contracts=contracts,
            schedules=schedules,
            publish_targets=publish_targets,
            join_key_policies=join_key_policies,
            pipeline_source_map=pipeline_source_map,
        )
        self.source_instances.upsert(instance_name, source_template_name, source_name, data_family, canonical_contract_name, schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name, is_enabled, metadata or {})
        artifacts = self.artifacts.write_source_instance(instance_name, source_template_name, source_name, data_family, canonical_contract_name, schedule_policy_name, publish_target_name, join_key_policy_name, pipeline_name, is_enabled, metadata or {})
        self.audit.record("save_source_instance", instance_name, status="ok", metadata={"artifacts": artifacts})

    def list_source_instances(self):
        return self.source_instances.list_all()

    def runtime_plan_for_date(self, year, month, day):
        plan = self.runtime_scheduler.plan_for_date(year, month, day)
        self.audit.record("runtime_plan_for_date", f"{year:04d}-{month:02d}-{day:02d}", status="ok", metadata={"items": len(plan)})
        return plan

    def run_source_instance_e2e(self, instance_name, year, month, day):
        result = self.e2e.run_source_instance(instance_name, year, month, day)
        self.audit.record("run_source_instance_e2e", instance_name, status=result.get("status", "unknown"), metadata=result)
        return result


    def save_knowledge_asset(self, asset_name, domain, asset_type, location_hint, tags=None, summary="", metadata=None):
        artifacts = self.artifacts.write_knowledge_asset(asset_name, domain, asset_type, location_hint, tags or [], summary, metadata or {})
        self.audit.record("save_knowledge_asset", asset_name, status="ok", metadata={"artifacts": artifacts, "domain": domain})
        return artifacts

    def list_knowledge_assets(self):
        return self.artifacts.list_knowledge_assets()


    def delete_source(self, name):
        self.sources.delete(name)
        self.audit.record("delete_source", name, status="ok")

    def delete_project(self, name):
        self.projects.delete(name)
        self.audit.record("delete_project", name, status="ok")
