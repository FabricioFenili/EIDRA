from pathlib import Path

from quant_macro_os.control_plane.services.diff_service import DiffService
from quant_macro_os.control_plane.services.repo_browser import RepoBrowser

def test_repo_browser_and_diff(tmp_path: Path):
    file_path = tmp_path / "module.py"
    file_path.write_text("x = 1\n", encoding="utf-8")
    browser = RepoBrowser(tmp_path)
    assert "module.py" in browser.list_files()
    diff = DiffService().diff_for_file(tmp_path, "module.py", "x = 2\n")
    assert "module.py:current" in diff
    assert "module.py:proposed" in diff
