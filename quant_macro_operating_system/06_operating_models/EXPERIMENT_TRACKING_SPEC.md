# EXPERIMENT TRACKING SPEC

## Purpose

Define how models, backtests, and quantitative experiments are recorded and audited.

## Every experiment must register

- `experiment_id`
- `experiment_name`
- `author`
- `timestamp`
- `dataset_version`
- `feature_set_version`
- `model_type`
- `parameter_set`
- `random_seed` when applicable

## Metrics to capture when relevant

- `annual_return`
- `volatility`
- `sharpe_ratio`
- `max_drawdown`
- `win_rate`

## Storage model

- experiment metadata in SQLite
- optional detailed artifacts under `11_runs/experiments/`

## Reproducibility rule

No experiment result should be considered valid without enough metadata to rerun it.
