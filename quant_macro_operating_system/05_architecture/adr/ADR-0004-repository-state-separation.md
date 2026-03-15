# ADR-0003 — Preserve repository-first, local-state-separated architecture

## Status
Accepted

## Context
The system must remain portable across machines without committing mutable operational state into Git.

## Decision
Version code, standards, contracts, and decisions in the repository; keep `data_lake/`, `state/`, `artifacts/`, `*.db`, and `*.duckdb` local and reconstructible.

## Consequences
The repository stays clean and portable. Bootstrapping and rebuild procedures become first-class requirements.
