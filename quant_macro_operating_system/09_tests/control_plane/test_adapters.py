from pathlib import Path
from quant_macro_os.control_plane.sources.adapters.api_adapter import APIAdapter
from quant_macro_os.control_plane.sources.adapters.file_adapter import FileAdapter
from quant_macro_os.control_plane.sources.adapters.manual_adapter import ManualAdapter
from quant_macro_os.control_plane.sources.adapters.database_adapter import DatabaseAdapter
from quant_macro_os.control_plane.sources.adapters.html_adapter import HTMLAdapter
from quant_macro_os.control_plane.sources.adapters.object_storage_adapter import ObjectStorageAdapter

def test_adapters_return_expected_shapes(tmp_path: Path):
    p = tmp_path / "sample.txt"
    p.write_text("hello", encoding="utf-8")
    assert APIAdapter().fetch({"endpoint": "x", "params": {}, "mock_payload": [1]})["source_type"] == "api"
    assert FileAdapter().fetch({"path": str(p)})["content"] == "hello"
    assert ManualAdapter().fetch({"records": [{"x": 1}]})["records"][0]["x"] == 1
    assert DatabaseAdapter().fetch({"query": "SELECT 1", "mock_rows": [{"a": 1}]})["rows"][0]["a"] == 1
    assert "html" in HTMLAdapter().fetch({"mock_html": "<html></html>"})
    assert ObjectStorageAdapter().fetch({"bucket": "b", "key": "k", "mock_content": "z"})["bucket"] == "b"
