import os
from pathlib import Path
from quant_macro_os.observability.logging.system_logger import get_logger

def test_v60_logger_can_write_with_repo_root(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("QMOS_REPO_ROOT", str(tmp_path))
    monkeypatch.delenv("QMOS_LOG_DIR", raising=False)
    logger = get_logger("v60_logger")
    logger.info("hello")
    assert logger.name == "v60_logger"
