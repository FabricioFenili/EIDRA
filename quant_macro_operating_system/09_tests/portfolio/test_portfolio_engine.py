from quant_macro_os.portfolio.optimization.expected_return_model import ExpectedReturnModel
from quant_macro_os.portfolio.optimization.portfolio_optimizer import PortfolioOptimizer
from quant_macro_os.portfolio.optimization.position_sizer import PositionSizer

def test_portfolio_engine_flow():
    expected = ExpectedReturnModel().estimate({"A": 0.2, "B": 0.1})
    weights = PortfolioOptimizer().optimize(expected)
    positions = PositionSizer().size_positions(weights, 1000.0)
    assert round(sum(weights.values()), 10) == 1.0
    assert round(sum(positions.values()), 10) == 1000.0
