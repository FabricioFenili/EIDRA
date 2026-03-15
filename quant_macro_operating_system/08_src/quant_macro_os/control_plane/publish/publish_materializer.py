from __future__ import annotations
import json
from pathlib import Path

from quant_macro_os.control_plane.services.paths import get_workdir

class PublishMaterializer:
    def __init__(self, workdir: Path | None = None):
        self.workdir = (workdir or get_workdir()).resolve()

    def materialize(self, model_name: str, instance_name: str, payload: dict) -> Path:
        out_dir = self.workdir / "platinum" / model_name
        out_dir.mkdir(parents=True, exist_ok=True)
        artifact = out_dir / f"{instance_name}.json"
        artifact.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return artifact
