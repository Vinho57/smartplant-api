import pandas as pd
import requests

class ApiHandler:
    def __init__(self, base_url: str, pot_id: int = 1):
        self.url = f"{base_url}/latest-today?pot_id={pot_id}"
        self.df = self._fetch_data()
        self.pot_id = pot_id

    def _parse_response(self, response):
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df["created"] = pd.to_datetime(df["created"])
            return df
        else:
            return pd.DataFrame()

    def _fetch_data(self):
        response = requests.get(self.url)
        return self._parse_response(response)

    def get_df(self):
        return self.df

    def get_sunlight_df(self):
        response = requests.get(f"http://localhost:5001/sunlight-30days?pot_id={self.pot_id}")
        return self._parse_response(response)