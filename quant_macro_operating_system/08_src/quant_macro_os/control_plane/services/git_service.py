from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict


class GitService:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()

    def status(self) -> Dict[str, object]:
        git_dir = self.repo_root / ".git"
        if not git_dir.exists():
            return {"available": False, "output": "git_not_initialized"}
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=str(self.repo_root),
            capture_output=True,
            text=True,
        )
        return {
            "available": True,
            "returncode": result.returncode,
            "output": result.stdout,
            "error": result.stderr,
        }
