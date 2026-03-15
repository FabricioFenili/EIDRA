# DATA SOURCES

## Purpose

Institutional catalog of approved data sources.

## Initial source catalog

### CVM
- fundamentals and filings
- quarterly / annual financial data

### Yahoo Finance
- daily price history
- dividends and split-adjusted market data when available

### Banco Central do Brasil
- rates, inflation, FX, credit, and macro indicators

### IBGE
- inflation, activity, national accounts, and structural indicators

### FRED
- international macro and rate series

### Commodity sources
- commodity price references from approved providers

## Governance fields per source

Every source entry should track:
- `source_name`
- `source_type`
- `domains_covered`
- `update_frequency`
- `ingestion_method`
- `responsible_pipeline`
- `licensing_or_access_notes` when relevant
