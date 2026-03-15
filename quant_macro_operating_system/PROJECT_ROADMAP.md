# PROJECT ROADMAP

## Objective

Provide a phased execution plan for building the Quant Macro Operating System without premature complexity or architectural drift.

## Phase 0 — Development Infrastructure

Completed / in-progress foundation:

- bootstrap discipline
- development workflow
- make commands
- architecture documentation
- ADR system
- data governance base documents

## Phase 1 — Data Platform

Deliverables:

- bronze / silver / gold conventions implemented in code
- local Parquet storage layout
- SQLite control plane tables
- DuckDB serving layer
- first production-ready ingestion pipelines

## Phase 2 — Feature Factory

Deliverables:

- feature registry table and metadata model
- feature build pipelines
- feature validation rules
- feature lineage tracking

## Phase 3 — Macro Intelligence Engine

Deliverables:

- macro dataset ingestion
- regime analytics foundation
- macro indicator marts
- scenario input datasets

## Phase 4 — Quant Research Engine

Deliverables:

- factor testing framework
- backtest scaffolds
- experiment tracking integration
- statistical validation utilities

## Phase 5 — Portfolio / Risk / Execution

Deliverables:

- allocation engine foundation
- risk constraints and monitoring
- execution planning abstractions
- performance attribution skeleton

## Phase 6 — Decision System

Deliverables:

- integrated signal-to-decision flow
- learning loop
- decision ledger linkage
- institutional review cycle

## Sequencing rule

Infrastructure before complexity.

Governance before scale.

Reproducibility before automation.
