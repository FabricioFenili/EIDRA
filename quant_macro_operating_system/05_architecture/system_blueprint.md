# System Blueprint

## Overview

The Quant Macro Operating System transforms data into institutional investment decisions through a structured pipeline.

Data → Features → Research → Portfolio → Risk → Execution → Performance

## Core Flow

### Data Platform

Responsibilities:

- ingest datasets
- validate data contracts
- maintain data lineage

Directory:

07_data_platform

### Feature Engineering

Responsibilities:

- build model-ready variables
- control data leakage
- maintain feature store

Directory:

08_src/quant_macro_os/features

### Quant Research

Responsibilities:

- signal discovery
- hypothesis testing
- backtesting

Directory:

08_src/quant_macro_os/research

### Macro Intelligence

Responsibilities:

- economic regime detection
- scenario analysis

Directory:

08_src/quant_macro_os/macro

### Portfolio Construction

Responsibilities:

- expected return estimation
- position sizing
- optimization

Directory:

08_src/quant_macro_os/portfolio

### Risk Engine

Responsibilities:

- drawdown control
- tail risk analysis
- liquidity stress testing

Directory:

08_src/quant_macro_os/risk

### Execution Engine

Responsibilities:

- order routing
- transaction cost modeling

Directory:

08_src/quant_macro_os/execution

### Performance & Learning

Responsibilities:

- performance attribution
- signal review
- model improvement

Directory:

08_src/quant_macro_os/performance

## Institutional Decision Loop

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

## Architecture Principles

- modular architecture
- contract-first interfaces
- reproducible pipelines
- evidence-driven decisions