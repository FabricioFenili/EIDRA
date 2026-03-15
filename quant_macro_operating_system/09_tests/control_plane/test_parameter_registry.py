from pathlib import Path
from quant_macro_os.control_plane.config.parameter_registry import ParameterRegistry

def test_parameter_registry_persists(tmp_path: Path):
    db_path = tmp_path / "control.db"
    registry = ParameterRegistry(db_path=db_path)
    registry.set("capital", 1000000)
    registry2 = ParameterRegistry(db_path=db_path)
    assert registry2.get("capital") == "1000000"
