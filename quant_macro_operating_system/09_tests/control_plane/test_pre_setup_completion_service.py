from pathlib import Path
from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.services.pre_setup_completion_service import PreSetupCompletionService

def test_pre_setup_completion_service_runs(tmp_path: Path):
    repo_root = Path(__file__).resolve().parents[2]
    db = tmp_path / "control.db"
    workdir = tmp_path / "workdir"
    api = ControlAPI(repo_root, db_path=db, workdir=workdir)
    result = PreSetupCompletionService(api).run(2026, 3, 8)
    assert result["status"] == "ok"
    assert result["smoke"]["result"]["published"] is True
    assert result["missing_count"] == 0
