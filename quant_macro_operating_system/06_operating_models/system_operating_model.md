# System Operating Model

## Overview

This document describes the operational cycle of the Quant Macro Operating System.
It defines how research, signals, portfolio decisions, and performance evaluation
are executed on a continuous basis.

## Research Cycle

1. Data ingestion
2. Feature generation
3. Hypothesis generation
4. Backtesting and validation
5. Signal approval

Responsible components:

- data_platform
- feature_engineering
- quant_research

## Signal Production Cycle

1. Feature update
2. Model evaluation
3. Signal generation
4. Risk validation

Responsible components:

- research
- risk

## Portfolio Construction Cycle

1. Expected return estimation
2. Portfolio optimization
3. Position sizing
4. Constraint validation

Responsible components:

- portfolio
- risk

## Execution Cycle

1. Order generation
2. Routing strategy
3. Transaction cost monitoring

Responsible components:

- execution

## Performance Review Cycle

1. Performance attribution
2. Signal evaluation
3. Model improvement proposals

Responsible components:

- performance
- research

## Institutional Decision Process

Founder request
↓
Agent Router
↓
Primary VP
↓
Supporting VPs
↓
Specialist analysis
↓
Council synthesis
↓
Institutional response

## Operational Principles

- reproducible pipelines
- risk-first decision making
- evidence-based research
- modular system components