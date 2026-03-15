# ADR-0003 — Separate Versioned Logic From Local Mutable State

## Status
Accepted

## Context
The project must remain portable across machines without committing mutable local state.

## Decision
Version repository logic, contracts, docs, schemas, and code. Keep mutable state local in `data_lake/`, `state/`, and `artifacts/`.

## Consequences
Benefits:
- cleaner Git history
- easier machine migration
- lower risk of corrupting version control with binary state
