from pathlib import Path
from quant_macro_os.control_plane.api.control_api import ControlAPI

def test_v60_can_delete_source(tmp_path: Path):
    api = ControlAPI(tmp_path, db_path=tmp_path / "control.db", workdir=tmp_path / "workdir")
    api.save_source("bcb_sgs", "api", {"base_url": "https://api.bcb.gov.br"})
    names = [row["name"] for row in api.list_sources()]
    assert "bcb_sgs" in names
    api.delete_source("bcb_sgs")
    names = [row["name"] for row in api.list_sources()]
    assert "bcb_sgs" not in names
