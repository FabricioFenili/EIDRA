from pathlib import Path
import pytest

from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.governance.bootstrap_governance_seed import seed_governance

def test_control_api_rejects_pipeline_without_registered_source(tmp_path: Path):
    db = tmp_path / "control.db"
    api = ControlAPI(tmp_path, db_path=db, workdir=tmp_path / "workdir")
    with pytest.raises(ValueError, match="pipeline_source_not_registered"):
        api.save_pipeline("bad_pipeline", "missing_source", ["source", "ingest", "publish"])

def test_control_api_rejects_source_instance_with_missing_contract(tmp_path: Path):
    db = tmp_path / "control.db"
    api = ControlAPI(tmp_path, db_path=db, workdir=tmp_path / "workdir")
    seed_governance(db_path=db, repo_root=tmp_path)
    api.save_source("fake_demo_source", "manual", {"records": [{"value": 1}]})
    api.save_pipeline("fake_demo_pipeline", "fake_demo_source", ["source", "ingest", "normalize", "validate", "publish"])
    with pytest.raises(ValueError, match="unknown_contract"):
        api.save_source_instance(
            "fake_demo_instance",
            "fake_demo_source",
            "fake_demo_source",
            "manual_research_inputs",
            "missing_contract",
            "daily_global_macro",
            "research_inputs_gold",
            "manual_research_join",
            "fake_demo_pipeline",
            True,
            {"mode": "test"},
        )

def test_control_api_rejects_source_instance_with_pipeline_source_mismatch(tmp_path: Path):
    db = tmp_path / "control.db"
    api = ControlAPI(tmp_path, db_path=db, workdir=tmp_path / "workdir")
    seed_governance(db_path=db, repo_root=tmp_path)
    api.save_source("source_a", "manual", {"records": [{"value": 1}]})
    api.save_source("source_b", "manual", {"records": [{"value": 2}]})
    api.save_pipeline("pipeline_a", "source_a", ["source", "ingest", "normalize", "validate", "publish"])
    with pytest.raises(ValueError, match="pipeline_source_mismatch"):
        api.save_source_instance(
            "instance_b",
            "source_b",
            "source_b",
            "manual_research_inputs",
            "manual_research_note_v1",
            "daily_global_macro",
            "research_inputs_gold",
            "manual_research_join",
            "pipeline_a",
            True,
            {"mode": "test"},
        )
