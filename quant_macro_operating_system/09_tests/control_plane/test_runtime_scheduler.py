from pathlib import Path

from quant_macro_os.control_plane.governance.schedule_policy_registry import SchedulePolicyRegistry
from quant_macro_os.control_plane.runtime.source_instance_registry import SourceInstanceRegistry
from quant_macro_os.control_plane.runtime.runtime_scheduler import RuntimeScheduler

def test_runtime_scheduler_plans_enabled_business_daily_instance(tmp_path: Path):
    db = tmp_path / "control.db"
    SchedulePolicyRegistry(db_path=db).upsert("business_daily_reference", "business_daily", "scheduled", "24h", "UTC", "09:00", {})
    SourceInstanceRegistry(db_path=db).upsert(
        "petax_bacen_sgs",
        "bacen_sgs",
        "petax_bacen_sgs",
        "macro_time_series",
        "time_series_numeric_v1",
        "business_daily_reference",
        "macro_reference_series",
        "macro_time_series_join",
        "bacen_macro_pipeline",
        True,
        {},
    )
    scheduler = RuntimeScheduler(db_path=db)
    plan = scheduler.plan_for_date(2026, 3, 9)  # Monday
    assert len(plan) == 1
    assert plan[0]["instance_name"] == "petax_bacen_sgs"
