import sys
from typing import Any
from pysrc import intern


class DataClient:
    def __init__(self) -> None:
        self.data_client = intern.DataClient()

    def get_data(self, symbol: str) -> Any:
        return self.data_client.get_data(symbol)
