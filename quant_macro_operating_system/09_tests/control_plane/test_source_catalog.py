from quant_macro_os.control_plane.sources.source_catalog_service import SourceCatalogService

def test_source_catalog_has_required_domains():
    service = SourceCatalogService()
    categories = service.list_categories()
    assert "central_banks_and_macro" in categories
    assert "market_prices_and_assets" in categories
    assert "fundamentals_and_regulatory" in categories
    assert "commodities_and_supply_chains" in categories
    assert "alternative_and_systemic_risk" in categories
    assert "internal_operational_sources" in categories

def test_source_catalog_templates_have_required_fields():
    required = {
        "template_name","source_type","provider","category","jurisdiction","asset_scope",
        "endpoint_or_path","auth_mode","params_schema","pagination_mode","rate_limit_policy",
        "freshness_expectation","raw_contract","normalized_contract","quality_checks",
        "id_keys","time_keys","mock_payload","owner_vp","owner_directorate"
    }
    for row in SourceCatalogService().list_templates():
        assert required.issubset(set(row.keys()))
