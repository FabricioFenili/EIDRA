# ARCHITECTURE

## System identity

Quant Macro Operating System is an institutional multi-agent factory for data, signals, macro intelligence, portfolio construction, risk governance, execution, and learning.

## Architectural principles

- explicit governance
- modular design
- low coupling
- reproducibility
- auditability
- local-first, low-cost operation
- upgrade path to heavier infrastructure only when justified

## Core technical stack

### Canonical storage
- Parquet

### Analytical serving
- DuckDB

### Control plane and registries
- SQLite

## Responsibility split

- **Parquet** stores canonical datasets across bronze, silver, and gold
- **DuckDB** queries gold-layer data and serves analytical use cases
- **SQLite** stores ledgers, registries, metadata, pipeline runs, feature registry, and experiment tracking

## System layers

### Governance layer
- `00_governance/`
- `01_constitutions/`
- `02_vps/`

### Contract layer
- `03_interfaces/`
- `04_ledgers_and_registries/`

### Architecture and operating models
- `05_architecture/`
- `06_operating_models/`

### Data platform layer
- `07_data_platform/`

### Executable source code
- `08_src/`

### Tests and knowledge work
- `09_tests/`
- `10_notebooks/`
- `11_runs/`
- `12_docs/`

## Data platform architecture

```text
Source
  -> Bronze (raw parquet)
  -> Silver (validated / standardized parquet)
  -> Gold (analytics-ready parquet)
  -> DuckDB serving / marts
```

SQLite stores the control plane for datasets, pipeline runs, feature registry, experiments, and future decision-support metadata.

## Agent architecture

```text
Founder / Chief Architect
  -> Executive Governance
  -> VP Council
  -> Directorates
  -> Superintendencies
  -> Managers
  -> Specialists
```

The repository documents the institutional organization explicitly before expanding execution logic.

## Local state policy

The repository versions standards, contracts, code, and decisions.

The local machine owns mutable state:

```text
data_lake/
state/
artifacts/
```

## Evolution strategy

The system evolves in layers:

1. development discipline and reproducibility
2. data platform implementation
3. feature factory
4. macro intelligence engine
5. quant research engine
6. portfolio / risk / execution integration
7. decision system and learning loop

## Architectural constraint

Do not introduce heavier infrastructure simply because it exists. Introduce it only when there is a demonstrated bottleneck, operational requirement, or measurable edge.
