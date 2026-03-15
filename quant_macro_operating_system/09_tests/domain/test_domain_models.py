from quant_macro_os.domain.assets.models import Asset

def test_asset_model():
    asset = Asset("a1", "BBAS3", "equity", "BRL", "BR", "B3")
    assert asset.ticker == "BBAS3"
