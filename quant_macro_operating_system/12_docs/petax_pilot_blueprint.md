# Petax Pilot Blueprint

## Why Petax first
Petax is an excellent first production source because it is:
- macro relevant
- time-series based
- scheduleable
- easy to validate
- useful across macro, FX, and risk workflows

## Target route
source_instance: petax_bacen_sgs
-> data_family: macro_time_series
-> contract: time_series_numeric_v1
-> schedule_policy: business_daily_reference
-> publish_target: macro_reference_series
-> platinum output: platinum_macro_reference_series

## Acceptance criteria
- source instance registered
- source eligible on business day
- pipeline exists
- execution plan includes source
- pipeline run recorded
- publish target declared
- audit event written
