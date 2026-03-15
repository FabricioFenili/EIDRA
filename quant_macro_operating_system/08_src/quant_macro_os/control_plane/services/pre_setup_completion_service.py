from __future__ import annotations
from pathlib import Path
from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.services.role_knowledge_routing_service import RoleKnowledgeRoutingService
from quant_macro_os.control_plane.services.startup_smoke_service import StartupSmokeService

class PreSetupCompletionService:
    def __init__(self, api: ControlAPI):
        self.api = api
        self.role_knowledge = RoleKnowledgeRoutingService(api.repo_root)

    def run(self, year: int, month: int, day: int) -> dict:
        smoke = StartupSmokeService(self.api).run(year, month, day)
        role_results = self.role_knowledge.validate_all()
        missing = [r for r in role_results if r["status"] != "ok"]
        return {
            "status": "ok" if smoke["status"] == "ok" and not missing else "fail",
            "smoke": smoke,
            "role_knowledge": role_results,
            "missing_count": len(missing),
        }
