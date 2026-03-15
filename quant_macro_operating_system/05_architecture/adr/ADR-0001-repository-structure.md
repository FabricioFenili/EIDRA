# ADR-0001 — Adopt Parquet + DuckDB + SQLite data stack

## Status
Accepted

## Context
The system is being built local-first on modest hardware. It needs analytical performance, low cost, portability, and clean separation of concerns without premature infrastructure.

## Decision
Adopt:

- Parquet for canonical bronze/silver/gold dataset storage
- DuckDB for analytical serving and local marts
- SQLite for registries, ledgers, metadata, and experiment / pipeline tracking

## Consequences
This keeps the stack lightweight and productive now, while preserving future migration paths to heavier infrastructure if justified by real bottlenecks.
