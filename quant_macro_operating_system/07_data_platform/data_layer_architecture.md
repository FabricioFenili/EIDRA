# Data Layer Architecture

Canonical flow:

raw -> bronze -> silver -> gold -> feature_store

## Raw
Immutable external source captures.

## Bronze
Schema-normalized ingestion outputs.

## Silver
Clean, validated, source-integrated tables.

## Gold
Analytics-ready curated datasets.

## Feature Store
Model-ready, versioned features for research and signal generation.

## Principles
- immutable raw storage
- contract-first ingestion
- lineage tracking
- reproducible transformations
- stable analytical layers
