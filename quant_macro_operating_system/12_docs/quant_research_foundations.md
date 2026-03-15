# Quant Research Foundations

## Purpose
Formalize the first scientific principles that the system must respect when moving from data factory into feature, research, and model factories.

## Foundational variable zero
The first irreducible variable of quantitative research is **return**.

Price alone is not the direct object of quantitative decision-making.
The research object is the transformation of price into a measurable payoff process.

## Canonical definitions

Let `P_t` be the asset price at time `t`.

### Simple return
`R_t = (P_t - P_{t-1}) / P_{t-1}`

### Log return
`r_t = ln(P_t / P_{t-1})`

## Institutional preference
The system should prefer **log returns** as the first canonical transformed series because:

- they are additive through time
- they stabilize many downstream formulations
- they simplify cumulative return reasoning
- they align with many econometric and continuous-time approximations

## Research target
The central object of quantitative research is:

`E[R_{t+1} | information_t]`

The system is not trying to predict prices directly.
It is trying to estimate the expected next-period return conditional on the information set available today.

## First-order consequences
From returns we derive:

- volatility
- excess return
- Sharpe-like signal quality
- drawdown
- momentum
- skewness
- kurtosis
- regime-conditioned behavior

## Decision rule warning
A raw rule such as:

- expected return > 0 => buy
- expected return < 0 => sell

is pedagogical only and is NOT sufficient for institutional decisions.

Real decision logic must include:

- expected return
- volatility
- confidence
- signal normalization
- allocation bands
- portfolio constraints
- risk budget
