# Adapter Contract Standard

Every adapter must expose a `fetch(config)` method and return an object that can be normalized into a canonical source payload.

## Adapter responsibilities
- authenticate if needed
- fetch source payload
- minimally parse
- preserve raw structure
- return metadata needed by the canonical ingestion layer

## Adapter must not
- implement business analytics
- implement research logic
- embed source-specific downstream assumptions

## Output pattern
- source_type
- payload/raw/content/rows
- optional metadata
