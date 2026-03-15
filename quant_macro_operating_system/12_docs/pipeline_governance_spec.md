# Pipeline Governance Specification

A pipeline in the Control Plane is a persistent, auditable object composed of:
- pipeline name
- source name
- ordered step list
- optional runtime parameters
- run history

## Canonical execution pattern
source -> ingest -> normalize -> validate -> curate -> feature -> publish

## Rules
- pipelines must be source-agnostic in architecture
- step execution must be logged
- pipeline runs must be persisted
- runtime parameters must be explicit
- failures must be auditable
