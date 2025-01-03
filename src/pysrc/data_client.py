import sys
from typing import Any, Optional
import requests
import json
import time

BASE_URL = "https://api.gemini.com/v1/trades/"


class DataClient:
    def __init__(self) -> None:
        self.data: dict[str, list[dict[str, Any]]] = {}
        self.last_timestampms: Optional[int] = None

    def _query_api(self, symbol: str) -> None:
        try:
            if self.last_timestampms is not None:
                response = requests.get(
                    BASE_URL + symbol, params={"timestamp": self.last_timestampms}
                )
            else:
                response = requests.get(BASE_URL + symbol)

            trade_history = response.json()

            try:
                self.last_timestampms = trade_history[0]["timestampms"]
            except Exception:
                print("No trades retrieved from API Query")

            self._parse_message(symbol, trade_history)

        except Exception as e:
            print(f"API Query Failed: {e}", file=sys.stderr)

    def _parse_message(self, symbol: str, trade_history: list[dict[str, Any]]) -> None:
        self.data[symbol] = trade_history

    def get_data(self, symbol: str) -> list[dict[str, Any]] | None:
        self._query_api(symbol)
        return self.data.get(symbol)
