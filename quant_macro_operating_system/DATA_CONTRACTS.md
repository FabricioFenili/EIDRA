# DATA CONTRACTS

## Purpose

Define the minimum institutional rules for datasets flowing through the Quant Macro Operating System.

## Naming standard

Datasets should follow a stable, descriptive pattern, such as:

```text
domain_entity_granularity
```

Examples:

- `macro_cpi_monthly`
- `equities_prices_daily`
- `fundamentals_income_statement_quarterly`

## Required metadata

Every dataset should define or be associated with:

- `dataset_name`
- `source`
- `granularity`
- `currency` when relevant
- `timezone` when relevant
- `update_frequency`
- `dataset_version`
- `ingestion_timestamp`
- `source_system`

## Schema stability rule

Do not silently break downstream consumers.

- do not remove columns without versioning
- do not change column meaning without versioning
- do not change types casually

## Layer semantics

### Bronze
- raw or near-raw capture
- minimal semantic transformation
- preserve source fidelity

### Silver
- standardized names
- cleaned types
- deduplicated when appropriate
- quality checks applied

### Gold
- analytics-ready
- cross-source joins allowed
- features and final aggregates allowed

## Quality gates

Before promoting a dataset to the next layer, validate:

- schema conformity
- key integrity
- plausibility of numeric ranges
- duplicate checks
- required field completeness

## Versioning rule

If a change breaks assumptions, create a new version instead of mutating old meaning.
