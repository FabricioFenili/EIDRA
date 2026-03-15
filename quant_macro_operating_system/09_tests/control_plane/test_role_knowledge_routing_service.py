from pathlib import Path
from quant_macro_os.control_plane.services.role_knowledge_routing_service import RoleKnowledgeRoutingService

def test_role_knowledge_routing_service_validates_all_roles():
    repo_root = Path(__file__).resolve().parents[2]
    service = RoleKnowledgeRoutingService(repo_root)
    results = service.validate_all()
    assert results
    assert all(r["status"] == "ok" for r in results), results
