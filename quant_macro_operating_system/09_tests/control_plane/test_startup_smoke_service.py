from pathlib import Path

from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.services.startup_smoke_service import StartupSmokeService

def test_startup_smoke_service_runs(tmp_path: Path):
    db = tmp_path / "control.db"
    workdir = tmp_path / "workdir"
    api = ControlAPI(tmp_path, db_path=db, workdir=workdir)
    result = StartupSmokeService(api).run(2026, 3, 8)
    assert result["status"] == "ok"
    assert result["result"]["published"] is True
