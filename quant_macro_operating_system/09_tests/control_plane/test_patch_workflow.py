from pathlib import Path

from quant_macro_os.control_plane.patch_manager.patch_applier import PatchApplier
from quant_macro_os.control_plane.patch_manager.patch_registry import PatchRegistry
from quant_macro_os.control_plane.patch_manager.patch_validator import PatchValidator

def test_patch_validator_accepts_valid_python(tmp_path: Path):
    target = tmp_path / "module.py"
    target.write_text("x = 1\n", encoding="utf-8")
    assert PatchValidator().validate("module.py", "x = 2\n", tmp_path).valid is True

def test_patch_validator_rejects_forbidden_operation(tmp_path: Path):
    target = tmp_path / "module.py"
    target.write_text("x = 1\n", encoding="utf-8")
    assert PatchValidator().validate("module.py", "import os\nos.remove('x')\n", tmp_path).valid is False

def test_patch_registry_and_applier(tmp_path: Path):
    target = tmp_path / "module.py"
    target.write_text("x = 1\n", encoding="utf-8")
    db_path = tmp_path / "control.db"
    registry = PatchRegistry(db_path=db_path)
    patch_id = registry.create("module.py", "x = 2\n")
    registry.approve(patch_id, "founder")
    workdir = tmp_path / "external_workdir"
    result = PatchApplier(workdir=workdir).apply(tmp_path, "module.py", "x = 2\n")
    assert result.applied is True
    assert Path(result.backup_path).exists()
