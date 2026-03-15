from quant_macro_os.agents.routing.router import AgentRouter, route_to_vp


def test_route_to_macro():
    env = route_to_vp("t1", "preciso analisar regime de inflação e liquidez")
    assert env.routed_vp == "vp_macro_intelligence"


def test_route_to_execution():
    env = route_to_vp("t2", "otimizar slippage e market impact das ordens")
    assert env.routed_vp == "vp_execution_microstructure"


def test_route_to_multiple_vps():
    env = AgentRouter().route("t3", "qual o impacto macro, risco e portfolio na alocação?")
    assert env.routed_vp in {"vp_macro_intelligence", "vp_portfolio_construction", "vp_risk_resilience"}
    assert len(env.supporting_vps) >= 1
