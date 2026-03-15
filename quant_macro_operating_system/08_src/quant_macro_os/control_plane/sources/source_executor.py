from __future__ import annotations
import json

from quant_macro_os.control_plane.sources.adapters.api_adapter import APIAdapter
from quant_macro_os.control_plane.sources.adapters.file_adapter import FileAdapter
from quant_macro_os.control_plane.sources.adapters.manual_adapter import ManualAdapter
from quant_macro_os.control_plane.sources.adapters.database_adapter import DatabaseAdapter
from quant_macro_os.control_plane.sources.adapters.html_adapter import HTMLAdapter
from quant_macro_os.control_plane.sources.adapters.object_storage_adapter import ObjectStorageAdapter

class SourceExecutor:
    ADAPTERS = {
        "api": APIAdapter,
        "file": FileAdapter,
        "manual": ManualAdapter,
        "database": DatabaseAdapter,
        "html": HTMLAdapter,
        "object_storage": ObjectStorageAdapter,
    }

    def execute(self, source_record):
        source_type = source_record["source_type"]
        config = json.loads(source_record["config_json"])
        adapter_cls = self.ADAPTERS.get(source_type)
        if adapter_cls is None:
            return {"status": "unsupported_source_type", "source_type": source_type}
        result = adapter_cls().fetch(config)
        result["status"] = "ok"
        result["source_name"] = source_record["name"]
        return result
