import json
from pathlib import Path

from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.governance.bootstrap_governance_seed import seed_governance

def test_fake_source_registration_e2e(tmp_path: Path):
    db = tmp_path / "control.db"
    workdir = tmp_path / "workdir"
    api = ControlAPI(tmp_path, db_path=db, workdir=workdir)

    seed_governance(db_path=db, repo_root=tmp_path)

    api.save_source("fake_demo_source", "manual", {"records": [{"value": 1}], "description": "fake"})
    api.save_pipeline("fake_demo_pipeline", "fake_demo_source", ["source", "ingest", "normalize", "validate", "publish"])
    api.save_source_instance(
        "fake_demo_instance",
        "fake_demo_source",
        "fake_demo_source",
        "manual_research_inputs",
        "manual_research_note_v1",
        "daily_global_macro",
        "research_inputs_gold",
        "manual_research_join",
        "fake_demo_pipeline",
        True,
        {"mode": "test"},
    )

    plan = api.runtime_plan_for_date(2026, 3, 8)
    assert any(item["instance_name"] == "fake_demo_instance" for item in plan)

    result = api.run_source_instance_e2e("fake_demo_instance", 2026, 3, 8)
    assert result["status"] == "ok"
    assert result["published"] is True

    published_path = Path(result["published_path"])
    assert published_path.exists()
    payload = json.loads(published_path.read_text(encoding="utf-8"))
    assert payload["instance_name"] == "fake_demo_instance"
    assert payload["publish_target_name"] == "research_inputs_gold"
