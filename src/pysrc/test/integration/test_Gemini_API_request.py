import pytest
from pysrc.data_client import DataClient
from pysrc import intern


def test_Gemini_API_request() -> None:
    client = DataClient()

    test_symbol = "btcusd"

    test_data = client.get_data(test_symbol)

    expected_keys = {
        "timestamp",
        "timestampms",
        "tid",
        "price",
        "amount",
        "exchange",
        "type",
    }

    for trade in test_data:
        for key in expected_keys:
            assert hasattr(trade, key)
