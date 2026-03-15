from quant_macro_os.agents.contracts.models import DelegationContract, TaskEnvelope


def test_task_envelope():
    env = TaskEnvelope(task_id="1", originating_user_request="test", routed_vp="vp_quant_research")
    assert env.routed_vp == "vp_quant_research"
    assert env.timestamps.timezone == "America/Sao_Paulo"


def test_delegation_contract():
    c = DelegationContract(
        delegator_level="vp",
        delegator_agent="vp_quant_research",
        receiver_level="director",
        receiver_agent="director_signal_discovery",
        delegated_scope="discover alpha signal",
        required_output="candidate signal pack",
        validation_rule="must satisfy contract",
        escalation_rule="escalate upward",
    )
    assert c.receiver_level == "director"
