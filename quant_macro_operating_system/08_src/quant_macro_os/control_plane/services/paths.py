from __future__ import annotations

import os
import tempfile
from pathlib import Path


def get_repo_root(default: Path | None = None) -> Path:
    env = os.getenv("QMOS_REPO_ROOT")
    if env:
        return Path(env).resolve()
    return (default or Path.cwd()).resolve()


def get_workdir(default_repo_root: Path | None = None) -> Path:
    env = os.getenv("QMOS_CONTROL_PLANE_WORKDIR")
    if env:
        return Path(env).resolve()
    base = Path(tempfile.gettempdir()) / "qmos_control_plane"
    if default_repo_root is not None:
        base = base / default_repo_root.resolve().name
    return base.resolve()


def get_db_path(default_repo_root: Path | None = None) -> Path:
    env = os.getenv("QMOS_CONTROL_PLANE_DB")
    if env:
        return Path(env).resolve()
    return get_workdir(default_repo_root) / "control_plane.db"
