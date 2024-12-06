import pytest
from pysrc.data_client import DataClient


def test_Gemini_API_request() -> None:
    client = DataClient()

    test_symbol = "btcusd"

    test_data = client.get_data(test_symbol)

    assert test_symbol in client.data

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
        assert expected_keys.issubset(trade.keys())
