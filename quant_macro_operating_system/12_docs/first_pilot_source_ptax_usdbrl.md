# First Pilot Source — BACEN PTAX USD/BRL

## Pilot objective
Use PTAX USD/BRL as the first vertical-slice source for validating the full industrial chain:

`source -> rawdata -> bronze -> silver -> gold -> platinum -> feature factory -> research factory`

## Why PTAX
- macroeconomically relevant
- long history
- relatively clean structure
- high interpretability
- useful for return, volatility, momentum, and regime research
- suitable for linking Brazil and global macro layers

## Canonical source identity
- source_name: `petax_bacen_sgs`
- source_type: `api`
- data_family: `macro_time_series`
- canonical_contract_name: `time_series_numeric_v1`
- schedule_policy_name: `business_daily_reference`
- publish_target_name: `macro_reference_series`
- join_key_policy_name: `macro_time_series_join`
- pipeline_name: `bacen_macro_pipeline`
- instance_name: `petax_bacen_sgs`

## First official transformed variables
- usd_brl_log_return
- usd_brl_volatility_20d
- usd_brl_momentum_20d
- usd_brl_momentum_60d
- usd_brl_momentum_120d
- usd_brl_drawdown
- usd_brl_skew_60d
- usd_brl_kurtosis_60d

## First research question
Determine whether PTAX contains persistent predictive structure under:
- time-series momentum
- volatility clustering
- macro regime interaction
