from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field


AgentLevel = Literal["founder", "cso", "cro", "vp", "director", "superintendent", "manager", "coordinator", "specialist"]
Priority = Literal["low", "normal", "high", "critical"]


class TimestampRecord(BaseModel):
    input_at: datetime = Field(default_factory=datetime.now)
    output_at: Optional[datetime] = None
    timezone: str = "America/Sao_Paulo"


class TaskEnvelope(BaseModel):
    task_id: str
    originating_user_request: str
    routed_vp: str
    supporting_vps: List[str] = Field(default_factory=list)
    routed_directorate: Optional[str] = None
    routed_superintendency: Optional[str] = None
    routed_management: Optional[str] = None
    routed_coordination: Optional[str] = None
    routed_specialists: List[str] = Field(default_factory=list)
    priority: Priority = "normal"
    artifact_expected: Optional[str] = None
    acceptance_criteria: List[str] = Field(default_factory=list)
    timestamps: TimestampRecord = Field(default_factory=TimestampRecord)
    metadata: Dict[str, str] = Field(default_factory=dict)


class DelegationContract(BaseModel):
    delegator_level: AgentLevel
    delegator_agent: str
    receiver_level: AgentLevel
    receiver_agent: str
    delegated_scope: str
    required_output: str
    validation_rule: str
    escalation_rule: str


class ManagerPlan(BaseModel):
    management_unit: str
    workflow_name: str
    ordered_micro_compounds: List[str]
    dependencies: List[str] = Field(default_factory=list)
    risk_points: List[str] = Field(default_factory=list)
    quality_gates: List[str] = Field(default_factory=list)
    downstream_consumers: List[str] = Field(default_factory=list)


class CoordinatorBatch(BaseModel):
    coordination_unit: str
    batch_id: str
    micro_compounds: List[str]
    sequence: List[str]
    checkpoints: List[str]
    merge_rule: str
    acceptance_rule: str


class SpecialistOutput(BaseModel):
    specialist_name: str
    artifact_type: str
    artifact_location: Optional[str] = None
    technical_summary: str
    assumptions: List[str] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)
    tests_executed: List[str] = Field(default_factory=list)
    ledger_updates: List[str] = Field(default_factory=list)


class InstitutionalResponse(BaseModel):
    task: TaskEnvelope
    primary_vp: str
    supporting_vps: List[str] = Field(default_factory=list)
    manager_plan: Optional[ManagerPlan] = None
    delegation_chain: List[DelegationContract] = Field(default_factory=list)
    specialist_outputs: List[SpecialistOutput] = Field(default_factory=list)
    council_synthesis: str
    final_response: str
