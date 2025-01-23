import time
import pandas as pd
from tqdm import tqdm
from pysrc.data_client import DataClient
from pysrc.model import LassoModel

client = DataClient()
model = LassoModel()

test_symbol = "btcusd"
time_sleep_sec = 10

for i in tqdm(range(11)):
    while True:
        test_data = client.get_data(test_symbol)
        parsed_data = [
            (trade.price, trade.amount, trade.type == "buy") for trade in test_data
        ]
        model.add_tick(parsed_data)
        time.sleep(time_sleep_sec)
        if len(parsed_data) != 0:
            break

num_predictions = 10

for i in tqdm(range(num_predictions)):
    model.predict()

    while True:
        test_data = client.get_data(test_symbol)
        parsed_data = [
            (trade.price, trade.amount, trade.type == "buy") for trade in test_data
        ]
        model.add_tick(parsed_data)

        time.sleep(time_sleep_sec)
        if len(parsed_data) != 0:
            break

targets = pd.read_csv("src/pysrc/targets.csv")
predictions = pd.read_csv("src/pysrc/predictions.csv")

data = pd.concat([targets, predictions], axis=1)
correlation = data["target"].corr(data["prediction"])

print(f"Correlation: {correlation:.5f}")
