from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Dict


class TestRunner:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()

    def run(self) -> Dict[str, object]:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(self.repo_root / "08_src")
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        result = subprocess.run(
            ["pytest", "-q", "-p", "no:cacheprovider", str(self.repo_root / "09_tests")],
            cwd=str(self.repo_root),
            env=env,
            capture_output=True,
            text=True,
        )
        return {
            "ok": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
