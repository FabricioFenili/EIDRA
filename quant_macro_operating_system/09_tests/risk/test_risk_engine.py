from quant_macro_os.risk.aggregation.risk_model import RiskModel
from quant_macro_os.risk.governance.drawdown_controller import DrawdownController
from quant_macro_os.risk.governance.exposure_manager import ExposureManager

def test_risk_engine_flow():
    positions = {"A": 600.0, "B": 400.0}
    risk = RiskModel().evaluate(positions)
    adjusted = ExposureManager().enforce_limits(risk["normalized_exposures"], 0.7)
    drawdown = DrawdownController().check_drawdown([100.0, 90.0, 110.0])
    assert "total_exposure" in risk
    assert adjusted["A"] <= 0.7
    assert "max_drawdown" in drawdown
