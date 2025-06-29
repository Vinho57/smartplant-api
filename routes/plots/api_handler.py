import pandas as pd
import requests

class ApiHandler:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _parse_response(self, response):
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df["created"] = pd.to_datetime(df["created"])
            return df
        else:
            return pd.DataFrame()

    def get_data(self, endpoint: str, pot_id: int):
        url = f"{self.base_url}/{endpoint}?pot_id={pot_id}"
        response = requests.get(url)
        return self._parse_response(response)