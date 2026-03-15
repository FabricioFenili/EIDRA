from pathlib import Path

from quant_macro_os.control_plane.api.control_api import ControlAPI

def test_v59_frontend_registrations_generate_artifacts(tmp_path: Path):
    api = ControlAPI(tmp_path, db_path=tmp_path / "control.db", workdir=tmp_path / "workdir")
    api.save_source("macro_source_demo", "manual", {"records": [{"value": 1}]})
    api.save_pipeline("macro_demo_pipeline", "macro_source_demo", ["source", "ingest", "normalize", "validate", "publish"])
    api.save_contract("manual_research_note_v1", "1.0.0", {"fields": [{"name": "value", "type": "number"}]}, {"required_fields": ["value"]})
    api.save_data_family("macro_manual_inputs", "Manual macro research inputs", "manual_research_note_v1", "event", "vp_quant_research", {})
    api.save_schedule_policy("daily_global_macro", "daily", "run_once_if_fresh", "24h", "UTC", "08:00", {})
    api.save_publish_target("research_inputs_gold", "gold", "manual_inputs", "Research inputs", {})
    api.save_join_key_policy("manual_research_join", "macro_manual_inputs", ["series_id"], "as_of_date", "left_latest_available", {})
    api.save_source_instance("macro_demo_instance", "macro_source_demo", "macro_source_demo", "macro_manual_inputs", "manual_research_note_v1", "daily_global_macro", "research_inputs_gold", "manual_research_join", "macro_demo_pipeline", True, {"mode": "test"})
    api.save_knowledge_asset("berkeley_macro_paper", "macro_economics", "paper", "12_docs/knowledge_pillars/literature_repository/macro_economics", ["macro", "research"], "registered through control plane", {})

    expected = [
        "07_data_platform/contracts/datasets/sources/macro_source_demo.yaml",
        "08_src/quant_macro_os/platform/data_sources/generated/macro_source_demo_source.py",
        "03_interfaces/canonical/pipeline_contracts/macro_demo_pipeline.yaml",
        "08_src/quant_macro_os/pipelines/data/generated/macro_demo_pipeline.py",
        "09_tests/pipelines/generated/test_macro_demo_pipeline.py",
        "07_data_platform/contracts/datasets/manual_research_note_v1.yaml",
        "04_ledgers_and_registries/data_families/macro_manual_inputs.yaml",
        "00_governance/runtime_artifacts/schedule_policies/daily_global_macro.yaml",
        "07_data_platform/serving/governance_ready/publish_targets/research_inputs_gold.yaml",
        "03_interfaces/mappings/join_key_policies/manual_research_join.yaml",
        "11_runs/source_instances/macro_demo_instance.yaml",
        "12_docs/knowledge_pillars/literature_repository/registrations/berkeley_macro_paper.yaml",
        "12_docs/knowledge_pillars/literature_repository/notes/berkeley_macro_paper.md",
    ]
    for rel in expected:
        assert (tmp_path / rel).exists(), rel
