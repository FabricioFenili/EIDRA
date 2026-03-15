from __future__ import annotations

from typing import List

from quant_macro_os.agents.contracts.models import (
    CoordinatorBatch,
    DelegationContract,
    InstitutionalResponse,
    ManagerPlan,
    SpecialistOutput,
    TaskEnvelope,
)
from quant_macro_os.agents.registry.agent_registry import AgentRegistry, DEFAULT_REGISTRY

DIRECTOR_BY_DOMAIN = {
    "research": "director_signal_discovery",
    "features": "director_feature_construction",
    "macro": "director_growth_inflation",
    "portfolio": "director_optimization_sizing",
    "risk": "director_tail_ruin_risk",
    "execution": "director_execution_algorithms",
    "performance": "director_performance_attribution",
}

SPECIALISTS_BY_DOMAIN = {
    "research": ["specialist_signal_screening", "specialist_econometric_diagnostics"],
    "features": ["specialist_feature_leakage_control"],
    "macro": ["specialist_regime_classifier"],
    "portfolio": ["specialist_kelly_optimizer"],
    "risk": ["specialist_tail_risk_model"],
    "execution": ["specialist_execution_cost_model"],
    "performance": ["specialist_postmortem_analyst"],
}

DOMAIN_BY_VP = {
    "vp_quant_research": "research",
    "vp_feature_engineering": "features",
    "vp_macro_intelligence": "macro",
    "vp_portfolio_construction": "portfolio",
    "vp_risk_resilience": "risk",
    "vp_execution_microstructure": "execution",
    "vp_performance_learning": "performance",
}


def make_handoff(
    delegator_level: str,
    delegator_agent: str,
    receiver_level: str,
    receiver_agent: str,
    delegated_scope: str,
    required_output: str,
) -> DelegationContract:
    return DelegationContract(
        delegator_level=delegator_level,
        delegator_agent=delegator_agent,
        receiver_level=receiver_level,
        receiver_agent=receiver_agent,
        delegated_scope=delegated_scope,
        required_output=required_output,
        validation_rule="must satisfy acceptance criteria and declared quality gates",
        escalation_rule="escalate one level up if contract cannot be satisfied",
    )


def build_manager_plan(name: str, workflow: str, micro_compounds: List[str]) -> ManagerPlan:
    return ManagerPlan(
        management_unit=name,
        workflow_name=workflow,
        ordered_micro_compounds=micro_compounds,
        dependencies=["task_envelope", "routing_decision"],
        risk_points=["ambiguous routing", "insufficient evidence", "scope mismatch"],
        quality_gates=["contract", "test", "ledger", "council review"],
        downstream_consumers=["vp_council"],
    )


def build_batch(coordination: str, batch_id: str, micro_compounds: List[str]) -> CoordinatorBatch:
    return CoordinatorBatch(
        coordination_unit=coordination,
        batch_id=batch_id,
        micro_compounds=micro_compounds,
        sequence=micro_compounds,
        checkpoints=["start", "specialist_merge", "validate", "council_review"],
        merge_rule="merge only contract-compliant outputs",
        acceptance_rule="all outputs must pass tests and declared validation",
    )


def orchestrate_task(task: TaskEnvelope, registry: AgentRegistry | None = None) -> InstitutionalResponse:
    registry = registry or DEFAULT_REGISTRY
    domain = DOMAIN_BY_VP[task.routed_vp]
    director = DIRECTOR_BY_DOMAIN[domain]
    specialists = list(SPECIALISTS_BY_DOMAIN[domain])
    task.routed_directorate = director
    task.routed_specialists = specialists

    plan = build_manager_plan(
        name=f"manager_{domain}_workflow",
        workflow=f"{domain}_institutional_workflow",
        micro_compounds=["scope_request", "delegate_analysis", "merge_outputs", "council_synthesize"],
    )

    delegation_chain = [
        make_handoff("vp", task.routed_vp, "director", director, task.originating_user_request, "directorate brief"),
    ]
    delegation_chain.extend(
        make_handoff("director", director, "specialist", specialist, task.originating_user_request, "specialist evidence pack")
        for specialist in specialists
    )

    specialist_outputs = [
        SpecialistOutput(
            specialist_name=specialist,
            artifact_type="analysis_note",
            technical_summary=f"{specialist} reviewed the request within {domain} domain scope.",
            assumptions=["initial request parsed from founder input"],
            constraints=["prototype orchestration without external market data"],
            tests_executed=["routing_consistency_check"],
            ledger_updates=["decision_ledger", "evidence_ledger"],
        )
        for specialist in specialists
    ]

    task.timestamps.output_at = task.timestamps.input_at
    council = f"Primary VP {task.routed_vp} consolidated {len(specialist_outputs)} specialist outputs for {domain}."
    final = (
        f"Institutional workflow prepared for {task.routed_vp}. "
        f"Directorate: {director}. Specialists: {', '.join(specialists)}."
    )
    return InstitutionalResponse(
        task=task,
        primary_vp=task.routed_vp,
        supporting_vps=task.supporting_vps,
        manager_plan=plan,
        delegation_chain=delegation_chain,
        specialist_outputs=specialist_outputs,
        council_synthesis=council,
        final_response=final,
    )
