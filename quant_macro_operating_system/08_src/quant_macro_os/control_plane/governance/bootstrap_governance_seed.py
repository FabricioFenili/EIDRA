from quant_macro_os.control_plane.governance.data_family_registry import DataFamilyRegistry
from quant_macro_os.control_plane.governance.contract_registry import ContractRegistry
from quant_macro_os.control_plane.governance.schedule_policy_registry import SchedulePolicyRegistry
from quant_macro_os.control_plane.governance.publish_target_registry import PublishTargetRegistry
from quant_macro_os.control_plane.governance.join_key_policy_registry import JoinKeyPolicyRegistry
from quant_macro_os.control_plane.runtime.source_instance_registry import SourceInstanceRegistry
from quant_macro_os.control_plane.sources.source_registry import SourceRegistry
from quant_macro_os.control_plane.pipeline.pipeline_registry import PipelineRegistry

def seed_governance(db_path=None, repo_root=None):
    families = DataFamilyRegistry(db_path=db_path, repo_root=repo_root)
    contracts = ContractRegistry(db_path=db_path, repo_root=repo_root)
    schedules = SchedulePolicyRegistry(db_path=db_path, repo_root=repo_root)
    targets = PublishTargetRegistry(db_path=db_path, repo_root=repo_root)
    joins = JoinKeyPolicyRegistry(db_path=db_path, repo_root=repo_root)

    contracts.upsert("time_series_numeric_v1", "v1", {"date": "date", "value": "float"}, ["non_empty", "date_parseable"], {})
    contracts.upsert("ohlcv_v1", "v1", {"timestamp": "datetime", "open": "float", "high": "float", "low": "float", "close": "float", "volume": "float"}, ["non_empty"], {})
    contracts.upsert("fundamentals_statement_v1", "v1", {"entity_id": "str", "reference_date": "date", "account": "str", "value": "float"}, ["non_empty"], {})
    contracts.upsert("risk_term_structure_v1", "v1", {"date": "date", "vix_front": "float", "vix_second": "float"}, ["non_empty"], {})
    contracts.upsert("manual_research_note_v1", "v1", {"record_id": "str", "payload": "dict"}, ["non_empty"], {})
    contracts.upsert("generic_rows_v1", "v1", {"row": "dict"}, ["non_empty"], {})

    families.upsert("macro_time_series", "Macro time series", "time_series_numeric_v1", "date", "vp_macro_intelligence", {})
    families.upsert("market_ohlcv", "Market OHLCV", "ohlcv_v1", "timestamp", "vp_quant_research", {})
    families.upsert("fundamentals_statements", "Fundamentals statements", "fundamentals_statement_v1", "reference_date", "vp_quant_research", {})
    families.upsert("commodity_reference_series", "Commodity series", "time_series_numeric_v1", "date", "vp_macro_intelligence", {})
    families.upsert("systemic_risk_series", "Systemic risk series", "risk_term_structure_v1", "date", "vp_risk_resilience", {})
    families.upsert("manual_research_inputs", "Manual research inputs", "manual_research_note_v1", "created_at", "vp_performance_learning", {})
    families.upsert("operational_ingestion_inputs", "Operational ingestion inputs", "generic_rows_v1", "ingested_at", "vp_data_platform", {})

    schedules.upsert("business_daily_reference", "business_daily", "scheduled", "24h", "UTC", "09:00", {})
    schedules.upsert("daily_global_macro", "daily", "scheduled", "24h", "UTC", "06:00", {})
    schedules.upsert("business_daily_market", "business_daily", "scheduled", "24h", "UTC", "18:00", {})
    schedules.upsert("quarterly_fundamentals", "quarterly", "scheduled", "90d", "UTC", "12:00", {})
    schedules.upsert("monthly_commodities", "monthly", "scheduled", "30d", "UTC", "10:00", {})
    schedules.upsert("on_demand_manual", "on_demand", "manual", "n_a", "UTC", "00:00", {})

    targets.upsert("macro_reference_series", "platinum", "platinum_macro_reference_series", "Integrated macro reference series", {})
    targets.upsert("market_prices_gold", "platinum", "platinum_market_prices", "Integrated market prices", {})
    targets.upsert("fundamentals_gold", "platinum", "platinum_fundamentals", "Integrated fundamentals", {})
    targets.upsert("commodities_gold", "platinum", "platinum_commodities", "Integrated commodities", {})
    targets.upsert("risk_signals_gold", "platinum", "platinum_risk_signals", "Integrated risk signals", {})
    targets.upsert("research_inputs_gold", "platinum", "platinum_research_inputs", "Manual research inputs", {})
    targets.upsert("operational_inputs_gold", "platinum", "platinum_operational_inputs", "Operational inputs", {})

    joins.upsert("macro_time_series_join", "macro_time_series", ["source_name"], "date", "calendar_align", {})
    joins.upsert("market_symbol_time_join", "market_ohlcv", ["symbol"], "timestamp", "market_calendar_align", {})
    joins.upsert("entity_period_join", "fundamentals_statements", ["entity_id"], "reference_date", "period_align", {})
    joins.upsert("risk_time_join", "systemic_risk_series", ["date"], "date", "calendar_align", {})
    joins.upsert("manual_research_join", "manual_research_inputs", ["record_id"], "created_at", "exact_match", {})
    joins.upsert("operational_row_join", "operational_ingestion_inputs", ["path"], "ingested_at", "exact_match", {})

def seed_source_instances(db_path=None, repo_root=None):
    instances = SourceInstanceRegistry(db_path=db_path, repo_root=repo_root)
    instances.upsert(
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
        {"example_series": "1", "pilot": "petax"},
    )

def seed_petax_pilot(db_path=None, repo_root=None):
    sources = SourceRegistry(db_path=db_path, repo_root=repo_root)
    pipelines = PipelineRegistry(db_path=db_path, repo_root=repo_root)
    sources.upsert("petax_bacen_sgs", "api", {
        "provider": "bacen",
        "endpoint": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{series}/dados",
        "params": {"formato": "json", "series": "1"},
        "mock_payload": [{"date": "2026-03-09", "value": "5.01"}],
    })
    pipelines.upsert("bacen_macro_pipeline", "petax_bacen_sgs", ["source", "ingest", "normalize", "validate", "publish"])
