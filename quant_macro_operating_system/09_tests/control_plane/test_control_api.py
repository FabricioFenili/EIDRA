from pathlib import Path

from quant_macro_os.control_plane.api.control_api import ControlAPI

def test_control_api_full_operational_flow(tmp_path: Path):
    target = tmp_path / "module.py"
    target.write_text("x = 1\n", encoding="utf-8")

    db_path = tmp_path / "control.db"
    workdir = tmp_path / "workdir"
    api = ControlAPI(tmp_path, db_path=db_path, workdir=workdir)

    api.save_project("main", "core project", "founder", "active")
    api.save_source("bacen_sgs", "api", {"series": ["11"]})
    api.set_parameter("universe", "BR_EQUITIES")
    api.save_pipeline("bacen_pipeline", "bacen_sgs", ["source", "ingest", "normalize", "publish"])

    assert api.list_projects()[0]["name"] == "main"
    assert api.list_sources()[0]["name"] == "bacen_sgs"
    assert api.get_parameters()["universe"] == "BR_EQUITIES"

    patch_id = api.stage_patch("module.py", "x = 2\n")
    api.approve_patch(patch_id, "founder")
    assert api.validate_patch("module.py", "x = 2\n") == "ok"
    assert "module.py:current" in api.preview_diff("module.py", "x = 2\n")
    backup = api.apply_patch(patch_id)
    assert Path(backup).exists()
    assert api.rollback_patch("module.py") is True

    pipeline_result = api.run_pipeline("bacen_pipeline", {"series": "11"})
    assert pipeline_result["status"] == "ok"
    assert len(api.get_audit_events()) >= 1
