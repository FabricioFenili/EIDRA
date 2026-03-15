# Signal Calibration Framework

## Purpose
Translate continuous model outputs into institutional decision bands.

## Problem
Research outputs are usually continuous.
Portfolio and risk decisions are usually discrete or semi-discrete.

Therefore the system requires an intermediate layer:

`expected_return -> normalization -> signal_strength -> decision_band -> portfolio_weight`

## Core principle
Do not use arbitrary thresholds.
Prefer thresholds based on statistical structure:

- z-scores
- quantiles
- posterior probabilities
- confidence intervals
- risk-adjusted expected return

## Reference normalization examples

### Example A: z-score normalization
`signal_strength = zscore(expected_return / expected_volatility)`

### Example B: quantile normalization
Map the signal into percentiles within the eligible asset universe.

## Institutional default decision bands

### Quantile mode
- 0-20   : very weak / avoid / strong underweight
- 20-40  : weak / underweight
- 40-60  : neutral
- 60-80  : strong / overweight
- 80-100 : very strong / concentrated overweight

### Z-score mode
- z < -2.0      : strong negative conviction
- -2.0 to -1.0  : moderate negative conviction
- -1.0 to  1.0  : neutral
-  1.0 to  2.0  : moderate positive conviction
- z >  2.0      : strong positive conviction

## Governance rules
Every decision band framework must specify:

- normalization method
- calibration window
- rebalance cadence
- turnover interaction
- risk budget interaction
- decay monitoring
- override and escalation protocol

## Required metadata
Each signal record must include:

- signal_name
- originating_model
- calibration_method
- reference_distribution
- decision_band
- confidence_level
- mapped_target_weight
