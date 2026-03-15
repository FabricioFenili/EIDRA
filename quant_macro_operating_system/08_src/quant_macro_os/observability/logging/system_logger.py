from __future__ import annotations

import logging
import os
import tempfile
from pathlib import Path


def _candidate_log_dirs() -> list[Path]:
    candidates: list[Path] = []
    env_dir = os.getenv("QMOS_LOG_DIR")
    if env_dir:
        candidates.append(Path(env_dir).expanduser())
    candidates.append(Path.home() / ".cache" / "qmos_logs")
    candidates.append(Path(tempfile.gettempdir()) / "qmos_logs")
    repo_root = os.getenv("QMOS_REPO_ROOT")
    if repo_root:
        candidates.append(Path(repo_root).expanduser() / ".qmos_runtime" / "logs")
    candidates.append(Path.cwd() / ".qmos_runtime" / "logs")
    return [c.resolve() for c in candidates]


def _resolve_log_file() -> Path:
    for directory in _candidate_log_dirs():
        try:
            directory.mkdir(parents=True, exist_ok=True)
            probe = directory / ".write_probe"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink(missing_ok=True)
            return directory / "system.log"
        except Exception:
            continue
    raise RuntimeError("no_writable_log_directory")


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    log_file = _resolve_log_file()
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
