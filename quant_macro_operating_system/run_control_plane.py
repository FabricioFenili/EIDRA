from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "quant_macro_operating_system" / "08_src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

os.environ.setdefault("PYTHONNOUSERSITE", "1")
os.environ.setdefault("QMOS_REPO_ROOT", str(ROOT / "quant_macro_operating_system"))
os.environ.setdefault("QMOS_CONTROL_PLANE_DB", str(ROOT / "control_plane.db"))
os.environ.setdefault("QMOS_CONTROL_PLANE_WORKDIR", str(ROOT / "qmos_control_plane_workdir"))

from streamlit.web.cli import main as streamlit_main

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        str(SRC / "quant_macro_os" / "control_plane" / "ui" / "streamlit_app.py"),
    ]
    raise SystemExit(streamlit_main())
