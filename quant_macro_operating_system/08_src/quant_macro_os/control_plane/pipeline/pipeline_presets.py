PIPELINE_PRESETS = {
    "bacen_macro_pipeline": {"source_name": "bacen_sgs", "steps": ["source", "ingest", "normalize", "validate", "publish"]},
    "bcb_expectations_pipeline": {"source_name": "bcb_expectativas", "steps": ["source", "ingest", "normalize", "validate", "publish"]},
    "fred_macro_pipeline": {"source_name": "fred", "steps": ["source", "ingest", "normalize", "validate", "publish"]},
    "world_bank_macro_pipeline": {"source_name": "world_bank", "steps": ["source", "ingest", "normalize", "validate", "publish"]},
    "yahoo_market_pipeline": {"source_name": "yahoo_finance", "steps": ["source", "ingest", "normalize", "validate", "feature", "publish"]},
    "cvm_fundamentals_pipeline": {"source_name": "cvm_cia_aberta", "steps": ["source", "ingest", "normalize", "validate", "curate", "publish"]},
    "manual_research_pipeline": {"source_name": "manual_research_input", "steps": ["source", "ingest", "curate", "feature", "publish"]},
}
