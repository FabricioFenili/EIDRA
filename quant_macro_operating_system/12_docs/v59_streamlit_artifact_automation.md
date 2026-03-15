# V59 Streamlit Artifact Automation

V59 upgrades the control plane from governed registration only to governed registration plus automatic artifact generation.

Canonical flow:
frontend form
-> governance validation
-> registry/database update
-> filesystem artifact generation
-> pipeline eligibility

Artifact destinations:
- sources -> 07_data_platform/contracts/datasets/sources/
- source python stubs -> 08_src/quant_macro_os/platform/data_sources/generated/
- pipelines -> 03_interfaces/canonical/pipeline_contracts/
- pipeline python stubs -> 08_src/quant_macro_os/pipelines/data/generated/
- pipeline generated tests -> 09_tests/pipelines/generated/
- data families -> 04_ledgers_and_registries/data_families/
- contracts -> 07_data_platform/contracts/datasets/
- schedule policies -> 00_governance/runtime_artifacts/schedule_policies/
- publish targets -> 07_data_platform/serving/governance_ready/publish_targets/
- join key policies -> 03_interfaces/mappings/join_key_policies/
- source instances -> 11_runs/source_instances/
- knowledge assets -> 12_docs/knowledge_pillars/literature_repository/
