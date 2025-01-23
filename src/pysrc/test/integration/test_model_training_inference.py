import pytest
import time
from tqdm import tqdm
from pysrc.data_client import DataClient
from pysrc.model import LassoModel


def test_model_training_inference() -> None:
    client = DataClient()
    model = LassoModel()

    test_symbol = "btcusd"

    for i in tqdm(range(11)):
        assert model.predict() is None
        while True:
            test_data = client.get_data(test_symbol)
            parsed_data = [
                (trade.price, trade.amount, trade.type == "buy") for trade in test_data
            ]
            model.add_tick(parsed_data)
            time.sleep(0.25)
            if len(parsed_data) != 0:
                break

    for i in tqdm(range(5)):
        assert model.predict() is not None
        while True:
            test_data = client.get_data(test_symbol)
            parsed_data = [
                (trade.price, trade.amount, trade.type == "buy") for trade in test_data
            ]
            model.add_tick(parsed_data)
            time.sleep(0.25)
            if len(parsed_data) != 0:
                break
