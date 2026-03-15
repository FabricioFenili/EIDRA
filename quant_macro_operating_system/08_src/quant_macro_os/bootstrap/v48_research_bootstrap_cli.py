from __future__ import annotations
import json
from quant_macro_os.control_plane.services.research_bootstrap_service import ResearchBootstrapService

def main():
    plan = ResearchBootstrapService().build_ptax_plan()
    print(json.dumps({
        "source_name": plan.source_name,
        "canonical_return_variable": plan.canonical_return_variable,
        "initial_features": plan.initial_features,
        "initial_signal": plan.initial_signal,
        "initial_model": plan.initial_model,
    }, indent=2))

if __name__ == "__main__":
    main()
