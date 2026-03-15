# Source Catalog Governance

The Source Catalog is the canonical institutional registry for all external and internal data origins.

Required domains:
- central_banks_and_macro
- market_prices_and_assets
- fundamentals_and_regulatory
- commodities_and_supply_chains
- alternative_and_systemic_risk
- internal_operational_sources

Mandatory fields:
- template_name
- source_type
- provider
- category
- jurisdiction
- asset_scope
- endpoint_or_path
- auth_mode
- params_schema
- pagination_mode
- rate_limit_policy
- freshness_expectation
- raw_contract
- normalized_contract
- quality_checks
- id_keys
- time_keys
- mock_payload
- owner_vp
- owner_directorate
