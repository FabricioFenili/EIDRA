from __future__ import annotations

from pathlib import Path
from typing import List


class RepoBrowser:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()

    def list_files(self) -> List[str]:
        files: List[str] = []
        for path in self.repo_root.rglob("*"):
            if path.is_file():
                rel = path.relative_to(self.repo_root).as_posix()
                if any(token in rel for token in ("__pycache__", ".pytest_cache")):
                    continue
                if rel.endswith((".pyc", ".bak", "system.log")):
                    continue
                files.append(rel)
        return sorted(files)

    def read_file(self, relative_path: str) -> str:
        return (self.repo_root / relative_path).read_text(encoding="utf-8")
