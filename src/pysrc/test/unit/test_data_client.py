import pytest
from unittest.mock import MagicMock
from pysrc.data_client import DataClient


def test__parse_message() -> None:
    client = DataClient()

    test_symbol = "btcusd"
    test_trade_history = [
        {
            "timestamp": 1,
            "timestampms": 1000,
            "tid": 5,
            "price": "90000.00",
            "amount": "0.05",
            "exchange": "gemini",
            "type": "buy",
        }
    ]

    client._parse_message(test_symbol, test_trade_history)

    assert test_symbol in client.data
    assert client.data[test_symbol] == test_trade_history


def test_get_data() -> None:
    client = DataClient()

    test_symbol = "btcusd"
    test_trade_history = [
        {
            "timestamp": 1,
            "timestampms": 1000,
            "tid": 5,
            "price": "90000.00",
            "amount": "0.05",
            "exchange": "gemini",
            "type": "buy",
        }
    ]

    client._query_api = MagicMock(
        side_effect=lambda symbol: client._parse_message(symbol, test_trade_history)
    )

    assert client.get_data(test_symbol) == test_trade_history
