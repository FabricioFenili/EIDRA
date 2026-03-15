# FEATURE REGISTRY SPEC

## Purpose

Define how quantitative features are named, versioned, validated, and traced.

## Mandatory metadata

- `feature_name`
- `category`
- `description`
- `formula_or_recipe`
- `source_datasets`
- `granularity`
- `version`
- `owner`
- `created_at`

## Categories

- fundamental
- technical
- macro
- market_structure
- derived

## Versioning rule

Any change in feature meaning or calculation requires a new version.

## Registry store

The authoritative registry should live in SQLite.

## Validation rule

Before a feature is promoted to production use, validate:
- missing value behavior
- range sanity
- reproducibility
- source lineage
