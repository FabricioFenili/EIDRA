from quant_macro_os.execution.cost.transaction_cost_model import TransactionCostModel
from quant_macro_os.execution.routing.execution_router import ExecutionRouter
from quant_macro_os.execution.routing.order_manager import OrderManager

def test_execution_engine_flow():
    orders = OrderManager().create_orders({"A": 100.0})
    routed = ExecutionRouter().route(orders)
    costs = TransactionCostModel().estimate(orders)
    assert routed["A"]["venue"] == "PRIMARY"
    assert costs["A"] > 0
