from quant_macro_os.agents.registry.agent_registry import build_default_registry


def test_registry_domain_lookup():
    registry = build_default_registry()
    research_vps = registry.by_domain("research", level="vp")
    assert research_vps[0].name == "vp_quant_research"


def test_registry_scope_search():
    registry = build_default_registry()
    matches = registry.search_scope("kelly optimization")
    assert any(agent.name == "specialist_kelly_optimizer" for agent in matches)
