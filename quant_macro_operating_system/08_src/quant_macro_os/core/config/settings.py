from dataclasses import dataclass
from pathlib import Path
import os
import tempfile

@dataclass(slots=True)
class RuntimeSettings:
    repository_root: Path
    workdir: Path
    environment_name: str
    timezone: str = "UTC"

    @classmethod
    def from_environment(cls) -> "RuntimeSettings":
        repo_root = Path(os.getenv("QMOS_REPO_ROOT", str(Path.cwd()))).resolve()
        workdir = Path(os.getenv("QMOS_WORKDIR", str(Path(tempfile.gettempdir()) / "qmos_runtime"))).resolve()
        env_name = os.getenv("QMOS_ENVIRONMENT", "pre_setup")
        timezone = os.getenv("QMOS_TIMEZONE", "UTC")
        return cls(repository_root=repo_root, workdir=workdir, environment_name=env_name, timezone=timezone)
