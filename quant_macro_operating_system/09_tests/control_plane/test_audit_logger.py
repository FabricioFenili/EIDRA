from pathlib import Path
from quant_macro_os.control_plane.audit.audit_logger import AuditLogger

def test_audit_logger_persists(tmp_path: Path):
    db_path = tmp_path / "control.db"
    logger = AuditLogger(db_path=db_path)
    logger.record("apply_patch", "ok", target_file="module.py", status="ok")
    logger2 = AuditLogger(db_path=db_path)
    events = logger2.all()
    assert len(events) >= 1
    assert events[0]["action"] == "apply_patch"
