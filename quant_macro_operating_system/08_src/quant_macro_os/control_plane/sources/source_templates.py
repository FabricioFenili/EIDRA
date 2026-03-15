from quant_macro_os.control_plane.sources.source_catalog import SOURCE_CATALOG
SOURCE_TEMPLATES = {
    key: {
        "source_type": value["source_type"],
        "config": {
            "provider": value["provider"],
            "endpoint": value["endpoint_or_path"],
            "params": value["params_schema"],
            "mock_payload": value["mock_payload"],
        },
    }
    for key, value in SOURCE_CATALOG.items()
}
