import sys
import requests
import json

BASE_URL = "https://api.gemini.com/v1/trades/"


class DataClient:
    def __init__(self) -> None:
        self.data = {}

    def _query_api(self, symbol: str) -> None:
        try:
            response = requests.get(BASE_URL + symbol)
            trade_history = response.json()
            self._parse_message(symbol, trade_history)
        except Exception as e:
            print(f"API Query Failed: {e}", file=sys.stderr)

    def _parse_message(self, symbol: str, trade_history: dict) -> None:
        self.data[symbol] = trade_history

    def get_data(self, symbol: str) -> None:
        self._query_api(symbol)
        print(self.data.get(symbol))
