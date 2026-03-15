from pathlib import Path
from datetime import date
from quant_macro_os.control_plane.governance.data_family_registry import DataFamilyRegistry
from quant_macro_os.control_plane.governance.contract_registry import ContractRegistry
from quant_macro_os.control_plane.governance.schedule_policy_registry import SchedulePolicyRegistry
from quant_macro_os.control_plane.governance.publish_target_registry import PublishTargetRegistry
from quant_macro_os.control_plane.governance.join_key_policy_registry import JoinKeyPolicyRegistry
from quant_macro_os.control_plane.services.execution_eligibility_engine import ExecutionEligibilityEngine

def test_canonical_governance_registries(tmp_path: Path):
    db = tmp_path / "control.db"
    DataFamilyRegistry(db_path=db).upsert("macro_time_series", "Macro series", "time_series_numeric_v1", "date", "vp_macro_intelligence", {})
    ContractRegistry(db_path=db).upsert("time_series_numeric_v1", "v1", {"date": "date", "value": "float"}, ["non_empty"], {})
    SchedulePolicyRegistry(db_path=db).upsert("business_daily_reference", "business_daily", "scheduled", "24h", "UTC", "09:00", {})
    PublishTargetRegistry(db_path=db).upsert("macro_reference_series", "platinum", "platinum_macro_reference_series", "Macro platinum target", {})
    JoinKeyPolicyRegistry(db_path=db).upsert("macro_time_series_join", "macro_time_series", ["source_name"], "date", "calendar_align", {})
    assert len(DataFamilyRegistry(db_path=db).list_all()) == 1
    assert len(ContractRegistry(db_path=db).list_all()) == 1
    assert len(SchedulePolicyRegistry(db_path=db).list_all()) == 1
    assert len(PublishTargetRegistry(db_path=db).list_all()) == 1
    assert len(JoinKeyPolicyRegistry(db_path=db).list_all()) == 1

def test_execution_eligibility_engine():
    engine = ExecutionEligibilityEngine()
    assert engine.should_run("daily", date(2026, 3, 8)) is True
    assert engine.should_run("business_daily", date(2026, 3, 8)) is False
    assert engine.should_run("monthly", date(2026, 4, 1)) is True
    assert engine.should_run("quarterly", date(2026, 4, 1)) is True
