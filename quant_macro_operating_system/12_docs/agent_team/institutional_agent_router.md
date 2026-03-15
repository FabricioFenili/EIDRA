# Institutional Agent Router v3

## Objective
Turn the governance design into an executable multi-agent operating core.

## Delivered components
- `AgentRegistry` with default institutional seed
- `AgentRouter` with primary and supporting VP routing
- `orchestrate_task` workflow with delegation chain and specialist outputs
- expanded pydantic contracts for timestamps and institutional response
- regression tests for router, registry and workflow

## Intended execution path
Founder input -> Router -> Primary VP -> Directorate -> Specialists -> VP council synthesis.

## Current constraints
This v3 release is an orchestration prototype. It does not yet connect to market data, ledgers, or execution venues.

## Recommended v4
- persistent ledger adapters
- external market data connectors
- policy based routing weights
- real output timestamp assignment at runtime
