from __future__ import annotations

PIPELINE_NAME = 'fake_demo_pipeline'
SOURCE_NAME = 'fake_demo_source'
STEPS = [
  "source",
  "ingest",
  "normalize",
  "validate",
  "publish"
]

def run(payload: dict | None = None) -> dict:
    return {
        'pipeline_name': PIPELINE_NAME,
        'source_name': SOURCE_NAME,
        'steps': STEPS,
        'payload': payload or {},
        'status': 'noop_ready',
    }
