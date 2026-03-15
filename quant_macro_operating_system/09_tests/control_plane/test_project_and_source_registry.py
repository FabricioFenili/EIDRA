from pathlib import Path

from quant_macro_os.control_plane.projects.project_registry import ProjectRegistry
from quant_macro_os.control_plane.sources.source_registry import SourceRegistry

def test_project_and_source_registry(tmp_path: Path):
    db_path = tmp_path / "control.db"
    projects = ProjectRegistry(db_path=db_path)
    sources = SourceRegistry(db_path=db_path)
    projects.upsert("main", "main project", "founder", "active")
    sources.upsert("bacen_sgs", "api", {"series": ["11"]})
    assert projects.list_all()[0]["name"] == "main"
    assert sources.list_all()[0]["name"] == "bacen_sgs"
