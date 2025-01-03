import pytest
import time
from pysrc.data_client import DataClient
from pysrc.model import LassoModel


def test_model_training_inference() -> None:
    client = DataClient()
    model = LassoModel()

    test_symbol = "btcusd"

    for i in range(10):
        test_data = client.get_data(test_symbol)
        parsed_data = [
            (float(trade["price"]), float(trade["amount"]), trade["type"] == "buy")
            for trade in test_data
        ]
        model.add_tick(parsed_data)
        assert model.predict() is None
        time.sleep(0.25)

    for i in range(10):
        test_data = client.get_data(test_symbol)
        parsed_data = [
            (float(trade["price"]), float(trade["amount"]), trade["type"] == "buy")
            for trade in test_data
        ]
        model.add_tick(parsed_data)
        assert model.predict() is not None
        time.sleep(0.25)
