from __future__ import annotations

import difflib
from pathlib import Path


class DiffService:
    def diff_for_file(self, repo_root: Path, relative_path: str, proposed: str) -> str:
        current = (repo_root / relative_path).read_text(encoding="utf-8")
        diff = difflib.unified_diff(
            current.splitlines(),
            proposed.splitlines(),
            fromfile=f"{relative_path}:current",
            tofile=f"{relative_path}:proposed",
            lineterm="",
        )
        return "\n".join(diff)
