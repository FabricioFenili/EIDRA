# Feature Factory Operating Model

## Mission
Transform Platinum datasets into governed, versioned, economically interpretable features.

## Flow
`platinum -> feature generation -> feature validation -> feature registry -> feature store -> research consumption`

## Mandatory feature families
1. return transforms
2. rolling statistics
3. momentum
4. drawdown and risk state
5. macro-derived features
6. regime-conditioned features

## Approval rule
A feature must not enter the active registry unless it has:
- an economic interpretation
- a reproducible formula
- source dependency lineage
- temporal integrity validation
- leakage review
- drift review

## Initial V48 approved features
- log_return
- rolling_volatility
- momentum_20d
- momentum_60d
- momentum_120d
- drawdown
- skewness_60d
- kurtosis_60d
