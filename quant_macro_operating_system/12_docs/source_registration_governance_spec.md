# Source Registration Governance Specification

Every source must declare:
- source_name
- source_type
- provider
- endpoint_or_path or equivalent config
- data_family
- canonical_contract_name
- schedule_policy_name
- publish_target_name
- join_key_policy_name
- pipeline_name
- enabled flag
- source instance name

## Governance rule
A source is not operational merely because it exists in the catalog.
It becomes operational only when a source instance binds:
- the source record
- the governance registries
- the runtime scheduler
- the pipeline
- the publish target
