from quant_macro_os.schemas.domain import AssetSchema

def test_asset_schema():
    asset = AssetSchema(asset_id="a1", ticker="BBAS3", asset_class="equity", currency="BRL", country="BR", exchange="B3")
    assert asset.asset_id == "a1"
