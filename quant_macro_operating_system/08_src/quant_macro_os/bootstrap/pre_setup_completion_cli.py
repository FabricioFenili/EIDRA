from __future__ import annotations
import json, os
from pathlib import Path
from quant_macro_os.control_plane.api.control_api import ControlAPI
from quant_macro_os.control_plane.services.pre_setup_completion_service import PreSetupCompletionService

def main():
    repo_root = Path(os.getenv("QMOS_REPO_ROOT", str(Path.cwd()))).resolve()
    db_path = Path(os.getenv("QMOS_CONTROL_PLANE_DB", str(repo_root / "control_plane.db"))).resolve()
    workdir = Path(os.getenv("QMOS_CONTROL_PLANE_WORKDIR", str(repo_root / "qmos_control_plane_workdir"))).resolve()
    api = ControlAPI(repo_root=repo_root, db_path=db_path, workdir=workdir)
    result = PreSetupCompletionService(api).run(2026, 3, 8)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
