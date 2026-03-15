from __future__ import annotations
from pathlib import Path

from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.governance.bootstrap_governance_seed import seed_governance

class StartupSmokeService:
    def __init__(self, api: ControlAPI):
        self.api = api

    def run(self, year: int, month: int, day: int) -> dict:
        seed_governance(db_path=self.api.projects.db_path if hasattr(self.api.projects, "db_path") else None, repo_root=self.api.repo_root)
        self.api.save_source(
            "fake_demo_source",
            "manual",
            {"records": [{"value": 1}], "description": "fake_source_for_smoke"},
        )
        self.api.save_pipeline("fake_demo_pipeline", "fake_demo_source", ["source", "ingest", "normalize", "validate", "publish"])
        self.api.save_source_instance(
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
            {"mode": "smoke"},
        )
        plan = self.api.runtime_plan_for_date(year, month, day)
        result = self.api.run_source_instance_e2e("fake_demo_instance", year, month, day)
        return {"status": "ok", "plan": plan, "result": result}
