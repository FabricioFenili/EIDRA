from __future__ import annotations

SOURCE_NAME = 'fake_demo_source'
SOURCE_TYPE = 'manual'

def get_source_definition() -> dict:
    return {
        'name': SOURCE_NAME,
        'source_type': SOURCE_TYPE,
        'config': {
  "records": [
    {
      "value": 1
    }
  ],
  "description": "fake_source_for_smoke"
},
    }
