# ADR-0005 — Adopt explicit data contracts and data platform standards

## Status
Accepted

## Context
A quant platform without explicit data contracts, source governance, pipeline standards, and feature registry rules becomes fragile and hard to audit.

## Decision
Treat `DATA_CONTRACTS.md`, `DATA_PLATFORM_SPEC.md`, `DATA_SOURCES.md`, `PIPELINE_STANDARDS.md`, and `FEATURE_REGISTRY_SPEC.md` as the minimum governance foundation for the platform layer.

## Consequences
Implementation must respect formal standards from the start, reducing ambiguity and rework later.
