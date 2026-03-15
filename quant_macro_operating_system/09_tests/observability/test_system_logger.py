from quant_macro_os.observability.logging.system_logger import get_logger

def test_get_logger_returns_logger():
    logger = get_logger("test_logger")
    logger.info("hello")
    assert logger.name == "test_logger"
