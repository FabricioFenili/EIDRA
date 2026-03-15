from quant_macro_os.research.engine.backtest_engine import BacktestEngine
from quant_macro_os.research.engine.experiment_runner import ExperimentRunner
from quant_macro_os.research.engine.signal_registry import SignalRegistry

def test_research_engine_components():
    runner = ExperimentRunner()
    result = runner.run("exp", {"window": 12})
    assert result.status == "executed"

    backtest = BacktestEngine().run_backtest("mom", [1.0, 2.0, 3.0])
    assert backtest.observations == 3

    signal = SignalRegistry().register("mom", "momentum")
    assert signal.name == "mom"
