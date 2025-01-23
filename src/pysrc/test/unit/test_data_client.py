import pytest
from pysrc.data_client import DataClient
from pysrc import intern


def test_get_data() -> None:
    client = intern.DataClient()

    test_symbol = "btcusd"

    assert client.get_data(test_symbol) is not None
