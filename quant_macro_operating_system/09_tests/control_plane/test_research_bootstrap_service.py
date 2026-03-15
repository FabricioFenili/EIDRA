from quant_macro_os.control_plane.services.research_bootstrap_service import ResearchBootstrapService

def test_research_bootstrap_service_builds_plan():
    svc = ResearchBootstrapService()
    plan = svc.build_ptax_plan()
    assert plan.source_name == "petax_bacen_sgs"
    assert plan.canonical_return_variable == "usd_brl_log_return"
    assert "usd_brl_momentum_20d" in plan.initial_features
    assert svc.signal_band(10) == "very_weak"
    assert svc.signal_band(35) == "weak"
    assert svc.signal_band(50) == "neutral"
    assert svc.signal_band(75) == "strong"
    assert svc.signal_band(90) == "extreme"
