from __future__ import annotations

import json
import re
from pathlib import Path


def _slug(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "artifact"


def _yaml_text(payload: dict) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


class ArtifactFactory:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()

    def _write(self, relative_path: str, payload: dict | str) -> str:
        target = self.repo_root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(payload, dict):
            target.write_text(_yaml_text(payload), encoding="utf-8")
        else:
            target.write_text(payload, encoding="utf-8")
        return str(target)

    def write_source(self, name: str, source_type: str, config: dict) -> dict:
        slug = _slug(name)
        yaml_path = self._write(
            f"07_data_platform/contracts/datasets/sources/{slug}.yaml",
            {"artifact_type": "source", "name": name, "source_type": source_type, "config": config},
        )
        py_content = (
            "from __future__ import annotations\n\n"
            f"SOURCE_NAME = {name!r}\n"
            f"SOURCE_TYPE = {source_type!r}\n\n"
            "def get_source_definition() -> dict:\n"
            "    return {\n"
            "        'name': SOURCE_NAME,\n"
            "        'source_type': SOURCE_TYPE,\n"
            f"        'config': {json.dumps(config, indent=2, ensure_ascii=False)},\n"
            "    }\n"
        )
        py_path = self._write(
            f"08_src/quant_macro_os/platform/data_sources/generated/{slug}_source.py",
            py_content,
        )
        return {"yaml_path": yaml_path, "python_stub_path": py_path}

    def write_pipeline(self, name: str, source_name: str, steps: list[str]) -> dict:
        slug = _slug(name)
        yaml_path = self._write(
            f"03_interfaces/canonical/pipeline_contracts/{slug}.yaml",
            {"artifact_type": "pipeline", "name": name, "source_name": source_name, "steps": steps},
        )
        py_content = (
            "from __future__ import annotations\n\n"
            f"PIPELINE_NAME = {name!r}\n"
            f"SOURCE_NAME = {source_name!r}\n"
            f"STEPS = {json.dumps(steps, indent=2, ensure_ascii=False)}\n\n"
            "def run(payload: dict | None = None) -> dict:\n"
            "    return {\n"
            "        'pipeline_name': PIPELINE_NAME,\n"
            "        'source_name': SOURCE_NAME,\n"
            "        'steps': STEPS,\n"
            "        'payload': payload or {},\n"
            "        'status': 'noop_ready',\n"
            "    }\n"
        )
        py_path = self._write(f"08_src/quant_macro_os/pipelines/data/generated/{slug}.py", py_content)
        test_content = (
            f"from quant_macro_os.pipelines.data.generated.{slug} import run\n\n"
            f"def test_generated_pipeline_{slug}_loads():\n"
            f"    result = run({{'probe': True}})\n"
            f"    assert result['pipeline_name'] == {name!r}\n"
            f"    assert result['status'] == 'noop_ready'\n"
        )
        test_path = self._write(f"09_tests/pipelines/generated/test_{slug}.py", test_content)
        return {"yaml_path": yaml_path, "python_stub_path": py_path, "test_path": test_path}

    def write_data_family(self, family_name: str, description: str, canonical_contract: str, grain: str, owner_vp: str, metadata: dict | None) -> dict:
        slug = _slug(family_name)
        yaml_path = self._write(
            f"04_ledgers_and_registries/data_families/{slug}.yaml",
            {
                "artifact_type": "data_family",
                "family_name": family_name,
                "description": description,
                "canonical_contract": canonical_contract,
                "grain": grain,
                "owner_vp": owner_vp,
                "metadata": metadata or {},
            },
        )
        return {"yaml_path": yaml_path}

    def write_contract(self, contract_name: str, schema_version: str, normalized_contract: dict, quality_checks: dict | list, metadata: dict | None) -> dict:
        slug = _slug(contract_name)
        yaml_path = self._write(
            f"07_data_platform/contracts/datasets/{slug}.yaml",
            {
                "artifact_type": "contract",
                "contract_name": contract_name,
                "schema_version": schema_version,
                "normalized_contract": normalized_contract,
                "quality_checks": quality_checks,
                "metadata": metadata or {},
            },
        )
        return {"yaml_path": yaml_path}

    def write_schedule_policy(self, policy_name: str, update_frequency: str, execution_policy: str, freshness_sla: str, timezone: str, first_eligible_time: str, metadata: dict | None) -> dict:
        slug = _slug(policy_name)
        yaml_path = self._write(
            f"00_governance/runtime_artifacts/schedule_policies/{slug}.yaml",
            {
                "artifact_type": "schedule_policy",
                "policy_name": policy_name,
                "update_frequency": update_frequency,
                "execution_policy": execution_policy,
                "freshness_sla": freshness_sla,
                "timezone": timezone,
                "first_eligible_time": first_eligible_time,
                "metadata": metadata or {},
            },
        )
        return {"yaml_path": yaml_path}

    def write_publish_target(self, target_name: str, layer: str, model_name: str, description: str, metadata: dict | None) -> dict:
        slug = _slug(target_name)
        yaml_path = self._write(
            f"07_data_platform/serving/governance_ready/publish_targets/{slug}.yaml",
            {
                "artifact_type": "publish_target",
                "target_name": target_name,
                "layer": layer,
                "model_name": model_name,
                "description": description,
                "metadata": metadata or {},
            },
        )
        return {"yaml_path": yaml_path}

    def write_join_key_policy(self, policy_name: str, data_family: str, key_columns: list[str], time_key: str, alignment_policy: str, metadata: dict | None) -> dict:
        slug = _slug(policy_name)
        yaml_path = self._write(
            f"03_interfaces/mappings/join_key_policies/{slug}.yaml",
            {
                "artifact_type": "join_key_policy",
                "policy_name": policy_name,
                "data_family": data_family,
                "key_columns": key_columns,
                "time_key": time_key,
                "alignment_policy": alignment_policy,
                "metadata": metadata or {},
            },
        )
        return {"yaml_path": yaml_path}

    def write_source_instance(self, instance_name: str, source_template_name: str, source_name: str, data_family: str, canonical_contract_name: str, schedule_policy_name: str, publish_target_name: str, join_key_policy_name: str, pipeline_name: str, is_enabled: bool, metadata: dict | None) -> dict:
        slug = _slug(instance_name)
        yaml_path = self._write(
            f"11_runs/source_instances/{slug}.yaml",
            {
                "artifact_type": "source_instance",
                "instance_name": instance_name,
                "source_template_name": source_template_name,
                "source_name": source_name,
                "data_family": data_family,
                "canonical_contract_name": canonical_contract_name,
                "schedule_policy_name": schedule_policy_name,
                "publish_target_name": publish_target_name,
                "join_key_policy_name": join_key_policy_name,
                "pipeline_name": pipeline_name,
                "is_enabled": is_enabled,
                "metadata": metadata or {},
            },
        )
        return {"yaml_path": yaml_path}

    def write_knowledge_asset(self, asset_name: str, domain: str, asset_type: str, location_hint: str, tags: list[str] | None = None, summary: str = "", metadata: dict | None = None) -> dict:
        slug = _slug(asset_name)
        yaml_path = self._write(
            f"12_docs/knowledge_pillars/literature_repository/registrations/{slug}.yaml",
            {
                "artifact_type": "knowledge_asset",
                "asset_name": asset_name,
                "domain": domain,
                "asset_type": asset_type,
                "location_hint": location_hint,
                "tags": tags or [],
                "summary": summary,
                "metadata": metadata or {},
            },
        )
        md_path = self._write(
            f"12_docs/knowledge_pillars/literature_repository/notes/{slug}.md",
            f"# {asset_name}\n\nDomain: {domain}\nAsset type: {asset_type}\nLocation hint: {location_hint}\n\n## Summary\n{summary or 'pending_summary'}\n\n## Tags\n{', '.join(tags or []) if tags else 'pending_tags'}\n",
        )
        return {"yaml_path": yaml_path, "note_path": md_path}

    def list_knowledge_assets(self) -> list[dict]:
        root = self.repo_root / "12_docs/knowledge_pillars/literature_repository/registrations"
        if not root.exists():
            return []
        rows = []
        for path in sorted(root.glob("*.yaml")):
            try:
                rows.append(json.loads(path.read_text(encoding="utf-8")))
            except Exception:
                rows.append({"artifact_type": "knowledge_asset", "asset_name": path.stem, "path": str(path)})
        return rows
