from quant_macro_os.platform.registries.metadata_registry import MetadataRegistry

def test_metadata_registry_registers_entities():
    registry = MetadataRegistry()
    registry.register_dataset("prices", "b3")
    registry.register_feature("momentum_12m", "12-month momentum")
    registry.register_pipeline("feature_pipeline", "platform")
    registry.register_experiment("exp_001", "baseline")
    assert registry.datasets["prices"] == "b3"
    assert registry.features["momentum_12m"] == "12-month momentum"
    assert registry.pipelines["feature_pipeline"] == "platform"
    assert registry.experiments["exp_001"] == "baseline"
