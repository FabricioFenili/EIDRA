from quant_macro_os.agents.routing.router import route_to_vp
from quant_macro_os.agents.workflows.handoff import orchestrate_task


def test_orchestrate_task_generates_delegations():
    task = route_to_vp("t100", "preciso de análise de inflação e crescimento")
    response = orchestrate_task(task)
    assert response.primary_vp == "vp_macro_intelligence"
    assert len(response.delegation_chain) >= 2
    assert response.specialist_outputs
