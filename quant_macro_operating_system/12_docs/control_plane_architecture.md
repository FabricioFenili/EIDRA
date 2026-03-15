# Control Plane Architecture

The Control Plane is the operator console of the Quant Macro Operating System.

## Objectives
- govern project parameters and operational state
- register data sources and pipelines
- orchestrate repeatable runs
- stage, validate, approve, apply, and rollback code changes
- provide persistent auditability

## Core Functional Domains
1. Project Governance
2. Source Registry
3. Pipeline Registry
4. Pipeline Execution
5. Patch Governance
6. Audit Ledger

## Operational Principle
No source registration, pipeline change, or patch application is considered valid unless:
- it is persisted
- it is auditable
- it is reversible
- it is testable
- it is visible in the UI

## UI Modules
- Overview
- Projects
- Sources
- Pipelines
- Patch Console
- Audit Ledger
