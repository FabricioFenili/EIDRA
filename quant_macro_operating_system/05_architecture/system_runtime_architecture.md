# System Runtime Architecture

## Overview

This document describes how the Quant Macro Operating System runs in production,
including orchestration, pipelines, execution layers, and system services.

## Runtime Layers

### 1. Data Ingestion Layer

Responsibilities:

- collect external datasets
- validate contracts
- store raw data

Components:

07_data_platform
pipelines/data

## 2. Feature Pipeline Layer

Responsibilities:

- transform raw data into model-ready features
- manage feature store

Components:

features
pipelines/features

## 3. Research Execution Layer

Responsibilities:

- run research experiments
- backtesting
- hypothesis validation

Components:

research
notebooks

## 4. Portfolio Engine

Responsibilities:

- combine signals
- generate portfolio weights

Components:

portfolio

## 5. Risk Control Layer

Responsibilities:

- validate risk exposure
- enforce drawdown and liquidity constraints

Components:

risk

## 6. Execution Layer

Responsibilities:

- translate portfolio decisions into orders
- optimize routing and transaction costs

Components:

execution

## 7. Performance Monitoring

Responsibilities:

- monitor performance
- record attribution
- generate improvement feedback

Components:

performance

## Orchestration

Runtime orchestration is handled through pipeline DAGs or workflow managers.

Typical structure:

data_pipeline → feature_pipeline → research_pipeline → portfolio_pipeline → execution_pipeline → performance_pipeline

## System Services

Supporting services include:

- logging
- metadata tracking
- experiment registry
- decision ledger
- evidence ledger

## Deployment Modes

The system can operate in:

- research mode
- backtest mode
- production execution mode

## Runtime Principles

- reproducible execution
- modular pipeline design
- observability-first architecture
- strict contract validation