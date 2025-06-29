import pandas as pd
import requests

def fetch_plot_data(url: str, column_map: dict) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    df["created"] = pd.to_datetime(df["created"])
    for new_col, old_col in column_map.items():
        df[new_col] = df[old_col]
    return df

def get_all_measurements_for_today(pot_id: int) -> pd.DataFrame:
    url = f"http://localhost:5001/latest-today?pot_id={pot_id}"
    return fetch_plot_data(url, {
        "temperature": "temperature",
        "soil_moisture": "ground_humidity",
        "luftfeuchtigkeit": "air_humidity"
    })

def get_sunlight_last_30_days(pot_id: int) -> pd.DataFrame:
    url = f"http://localhost:5001/sunlight-30days?pot_id={pot_id}"
    return fetch_plot_data(url, {
        "sunlight": "sunlight"
    })

def get_standard_layout(x_title: str, y_title: str, y_range=None, x_range=None) -> dict:
    return dict(
        xaxis=dict(
            title=x_title,
            tickformat="%H:%M",
            automargin=True,
            range=x_range if x_range is not None else ["00:00", "23:59"],
            nticks=6
        ),
        yaxis=dict(
            title=y_title,
            showgrid=True,
            gridcolor="lightgrey",
            gridwidth=1,
            range=y_range
        ),
        plot_bgcolor="white",
        font=dict(family="Arial", size=14),
        margin=dict(l=40, r=20, t=40, b=40),
    )
