# Quant Macro Operating System

Institutional multi-agent operating system for quant research, macro intelligence, feature engineering, portfolio construction, risk governance, execution, and performance learning.

## Mission

This repository is the software factory for building a reproducible, governed, low-friction systematic macro and quant platform. It is designed to start local-first on modest hardware and scale only when the edge justifies the added complexity.

## Design posture

- **Governance first**: architecture, contracts, and operating rules are explicit.
- **Local-first**: the default environment is a single technical founder working locally.
- **Reproducible**: code, standards, and decisions are versioned; mutable state is reconstructed.
- **Upgradeable**: the stack can evolve to heavier infrastructure without invalidating the operating model.

## Official data stack

- **Canonical storage**: Parquet
- **Analytical serving**: DuckDB
- **Control plane / registries / ledgers**: SQLite

This split keeps cost and complexity proportional to the current stage while preserving a clean migration path.

## Start here

1. Read `BOOTSTRAP.md`
2. Run `make bootstrap`
3. Run `make db-init`
4. Run `make test`
5. Follow `DEVELOPMENT_WORKFLOW.md`

## Core operating documents

### Root-level documents
- `BOOTSTRAP.md` — local machine initialization and environment setup
- `DEVELOPMENT_WORKFLOW.md` — branching, commits, pull requests, and delivery discipline
- `ARCHITECTURE.md` — technical constitution and responsibility split across layers
- `DATA_CONTRACTS.md` — dataset naming, schema stability, metadata, and promotion rules
- `PROJECT_ROADMAP.md` — phased execution sequence for building the system

### Architecture and governance
- `05_architecture/adr/ADR_INDEX.md` — ledger of accepted architecture decisions
- `05_architecture/adr/ADR_TEMPLATE.md` — template for new ADRs
- `05_architecture/adr/ADR-0001-data-stack.md` — Parquet + DuckDB + SQLite decision
- `05_architecture/adr/ADR-0002-agent-governance.md` — institutional multi-agent governance decision
- `05_architecture/adr/ADR-0003-repository-state-separation.md` — repository vs local state policy
- `05_architecture/adr/ADR-0004-development-workflow.md` — governed development workflow decision
- `05_architecture/adr/ADR-0005-data-governance-foundation.md` — data contracts and platform standards decision

### Data platform
- `07_data_platform/DATA_PLATFORM_SPEC.md` — bronze/silver/gold implementation rules
- `07_data_platform/DATA_SOURCES.md` — approved source catalog and governance fields
- `07_data_platform/PIPELINE_STANDARDS.md` — mandatory pipeline shape and logging rules
- `07_data_platform/FEATURE_REGISTRY_SPEC.md` — feature naming, versioning, and lineage rules
- `06_operating_models/EXPERIMENT_TRACKING_SPEC.md` — experiment and backtest registration standard

## Repository map

- `00_governance/` — project charter, organizational rules, naming, precedence
- `01_constitutions/` — strategic constitutions
- `02_vps/` — VP engines, directorates, and superintendencies
- `03_interfaces/` — contracts and schemas
- `04_ledgers_and_registries/` — ledgers, registries, and memory structures
- `05_architecture/` — technical architecture and ADRs
- `06_operating_models/` — end-to-end operating models and experiment governance
- `07_data_platform/` — data platform specifications, source catalog, and standards
- `08_src/` — executable source code
- `09_tests/` — automated tests
- `10_notebooks/` — exploratory and diagnostic notebooks
- `11_runs/` — run outputs and reviews
- `12_docs/` — supporting documentation

## Local state policy

The repository versions **logic, contracts, documentation, schemas, migrations, and standards**.

The local machine owns **mutable state**, including:

- `data_lake/`
- `state/`
- `artifacts/`
- `*.db`
- `*.duckdb`

These should not be committed.

## Makefile commands

- `make bootstrap` — create the venv, install dependencies, create local folders
- `make db-init` — initialize local SQLite and DuckDB files
- `make test` — run automated tests
- `make lint` — run lint checks
- `make format` — format Python code
- `make check` — run lint + tests
- `make clean` — remove caches and temporary artifacts

## Current implementation status

The repository already contains institutional architecture, agent routing, contracts, baseline tests, and the full governance foundation for the data platform.

The next implementation focus is **Phase 1 — Data Platform**:

- create control-plane tables in SQLite
- define first dataset contracts in code
- build first ingestion pipelines into bronze
- add silver standardization and quality checks
- expose first gold datasets through DuckDB

## Pre-Setup Completion Validation

Run:
`python -m quant_macro_os.bootstrap.pre_setup_completion_cli`

This validates:
- governance and role knowledge routing
- fake-source operational end-to-end chain
- pre-setup completion standard
