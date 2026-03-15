from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PatchValidationResult:
    valid: bool
    reason: str


class PatchValidator:
    FORBIDDEN_TOKENS = (
        "rm -rf",
        "shutil.rmtree(",
        "os.remove(",
        "os.rmdir(",
        "subprocess.run(",
        "subprocess.Popen(",
    )

    def validate(self, target_file: str, content: str, repo_root: Path) -> PatchValidationResult:
        if not target_file:
            return PatchValidationResult(False, "target_file_required")
        target_path = repo_root / target_file
        if not target_path.exists():
            return PatchValidationResult(False, "target_file_not_found")
        if any(token in content for token in self.FORBIDDEN_TOKENS):
            return PatchValidationResult(False, "forbidden_operation_detected")
        if target_path.suffix == ".py":
            try:
                compile(content, str(target_path), "exec")
            except Exception as exc:
                return PatchValidationResult(False, f"python_syntax_error:{exc}")
        return PatchValidationResult(True, "ok")
