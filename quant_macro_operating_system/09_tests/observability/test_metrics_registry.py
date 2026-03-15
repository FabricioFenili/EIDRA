from quant_macro_os.observability.metrics.registry import CORE_METRICS

def test_core_metrics_present():
    assert "data_freshness" in CORE_METRICS
