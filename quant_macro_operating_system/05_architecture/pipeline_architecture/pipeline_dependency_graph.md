# Pipeline Dependency Graph

data_pipeline -> feature_pipeline -> research_pipeline -> portfolio_pipeline -> risk_pipeline -> execution_pipeline -> performance_pipeline

macro_pipeline alimenta research_pipeline e portfolio_pipeline.
performance_pipeline alimenta feedback para research, portfolio e risk.
