from pathlib import Path

from quant_macro_os.core.orchestration.instance_chain import InstanceChainExecutor
from quant_macro_os.platform.marts.platinum_service import PlatinumService
from quant_macro_os.research.alpha.alpha_factory import AlphaFactory
from quant_macro_os.risk.stress.stress_engine import StressEngine
from quant_macro_os.execution.algorithms.base_algorithm import ExecutionAlgorithm
from quant_macro_os.control_plane.runtime.instance_call_chain_service import InstanceCallChainService

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_v42_operational_skeletons_exist():
    required = [
        "08_src/quant_macro_os/core/orchestration/instance_chain.py",
        "08_src/quant_macro_os/platform/marts/platinum_service.py",
        "08_src/quant_macro_os/research/alpha/alpha_factory.py",
        "08_src/quant_macro_os/risk/stress/stress_engine.py",
        "08_src/quant_macro_os/execution/algorithms/base_algorithm.py",
        "08_src/quant_macro_os/control_plane/runtime/instance_call_chain_service.py",
    ]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), rel

def test_v42_noop_methods_are_operational():
    plan = InstanceChainExecutor().plan("petax_bacen_sgs")
    assert plan.instance_name == "petax_bacen_sgs"
    assert InstanceChainExecutor().execute(plan)["status"] == "ok"

    ps = PlatinumService()
    ps.materialize_domain_model("demo", {"x": 1})
    assert ps.load_domain_model("demo") == {"x": 1}

    assert AlphaFactory().generate_candidates({"dataset": "x"})["status"] == "ok"
    assert StressEngine().run({"scenario": "base"})["status"] == "ok"
    assert ExecutionAlgorithm().schedule({"order": 1})["status"] == "ok"

    chain = InstanceCallChainService().build_chain("petax_bacen_sgs")
    assert len(chain) >= 1
