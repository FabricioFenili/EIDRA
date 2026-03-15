# DATA PLATFORM SPEC

## Official stack

- Canonical dataset storage: Parquet
- Analytical serving: DuckDB
- Control plane: SQLite

## Lake structure

```text
data_lake/
  bronze/
  silver/
  gold/
```

## Layer rules

### Bronze
- raw or near-raw ingestion
- preserve source fidelity
- minimal transformation

### Silver
- standardized column names
- consistent typing
- deduplicated when required
- data quality checks applied

### Gold
- analytics-ready datasets
- cross-source joins and derived metrics allowed
- stable consumption layer for research and dashboards

## Query model

DuckDB queries Parquet from gold directly.

## Control plane model

SQLite stores metadata such as datasets, pipeline runs, feature registry, and experiment references.

## Promotion rule

No dataset moves to the next layer without validation.
