from quant_macro_os.pipelines.data.generated.fake_demo_pipeline import run

def test_generated_pipeline_fake_demo_pipeline_loads():
    result = run({'probe': True})
    assert result['pipeline_name'] == 'fake_demo_pipeline'
    assert result['status'] == 'noop_ready'
