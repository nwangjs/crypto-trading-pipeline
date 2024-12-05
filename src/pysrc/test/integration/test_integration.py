import pytest
from pysrc.data_client import DataClient


def test_integration() -> None:
    client = DataClient()

    test_symbol = "btcusd"

    client.get_data(test_symbol)

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

    for trade in client.data[test_symbol]:
        assert expected_keys.issubset(trade.keys())
