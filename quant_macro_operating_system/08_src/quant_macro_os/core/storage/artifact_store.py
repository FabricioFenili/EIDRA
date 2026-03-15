import json
from pathlib import Path
from typing import Any

class ArtifactStore:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def put_json(self, relative_path: str, payload: dict[str, Any]) -> Path:
        target = self.root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return target

    def get_json(self, relative_path: str) -> dict[str, Any]:
        target = self.root / relative_path
        if not target.exists():
            return {}
        return json.loads(target.read_text(encoding="utf-8"))
