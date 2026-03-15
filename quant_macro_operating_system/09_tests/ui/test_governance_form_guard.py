from quant_macro_os.control_plane.ui.governance_form_guard import registration_readiness

def test_registration_readiness_blocks_when_dependencies_missing():
    result = registration_readiness(
        source_names=[],
        data_families=["macro_time_series"],
        contracts=["time_series_numeric_v1"],
        schedules=["business_daily_reference"],
        publish_targets=["macro_reference_series"],
        join_policies=["macro_time_series_join"],
        pipelines=["bacen_macro_pipeline"],
    )
    assert result["ready"] is False
    assert "sources" in result["missing"]

def test_registration_readiness_allows_when_everything_exists():
    result = registration_readiness(
        source_names=["petax_bacen_sgs"],
        data_families=["macro_time_series"],
        contracts=["time_series_numeric_v1"],
        schedules=["business_daily_reference"],
        publish_targets=["macro_reference_series"],
        join_policies=["macro_time_series_join"],
        pipelines=["bacen_macro_pipeline"],
    )
    assert result["ready"] is True
    assert result["missing"] == []
