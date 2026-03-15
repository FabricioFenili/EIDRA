# Model Factory Operating Model

## Mission
Train, validate, register, monitor, recalibrate, and retire models derived from research output.

## Flow
`research candidate -> training -> validation -> calibration -> model registry -> signal emission -> decay monitoring -> retirement`

## Initial model scope for V48
Start with low-complexity, high-interpretability models:
- autoregressive baselines
- rolling linear models
- logistic regime classifiers
- ARIMA with macro regressors where applicable

## Institutional warning
No model enters the active layer solely because it backtested well.
It must also satisfy:
- diagnostic quality
- robustness review
- interpretability threshold
- turnover feasibility
- risk fit
- signal calibration discipline
