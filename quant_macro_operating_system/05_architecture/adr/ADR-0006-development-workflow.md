# ADR-0004 — Use governed development workflow with main/develop/feature branches

## Status
Accepted

## Context
Without an explicit workflow, repositories drift into ambiguous commits, direct pushes to stable branches, and undocumented structural changes.

## Decision
Adopt a governed workflow based on `main`, `develop`, and typed working branches, with required formatting, linting, testing, and ADR updates for structural changes.

## Consequences
The repository gains traceability and safer change integration at the cost of a small amount of process overhead.
