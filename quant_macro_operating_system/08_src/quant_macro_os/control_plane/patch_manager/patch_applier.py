from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from quant_macro_os.control_plane.services.paths import get_workdir


@dataclass(frozen=True)
class ApplyResult:
    applied: bool
    backup_path: str


class PatchApplier:
    def __init__(self, workdir: Path | None = None):
        self.workdir = workdir or get_workdir()

    def apply(self, repo_root: Path, target_file: str, content: str) -> ApplyResult:
        repo_root = repo_root.resolve()
        target_path = repo_root / target_file
        backup_dir = self.workdir / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = backup_dir / f"{target_file.replace('/', '__')}.bak"
        backup_path.write_text(target_path.read_text(encoding="utf-8"), encoding="utf-8")
        target_path.write_text(content, encoding="utf-8")
        return ApplyResult(applied=True, backup_path=str(backup_path))

    def rollback(self, repo_root: Path, target_file: str) -> bool:
        repo_root = repo_root.resolve()
        target_path = repo_root / target_file
        backup_path = self.workdir / "backups" / f"{target_file.replace('/', '__')}.bak"
        if not backup_path.exists():
            return False
        target_path.write_text(backup_path.read_text(encoding="utf-8"), encoding="utf-8")
        return True
