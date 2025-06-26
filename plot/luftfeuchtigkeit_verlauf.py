import os
import requests
import plotly.graph_objects as go
import pandas as pd

USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

if USE_DUMMY:
    data = {
        "created": pd.to_datetime([
            "2025-06-25 06:00", "2025-06-25 07:00", "2025-06-25 08:00", "2025-06-25 09:00",
            "2025-06-25 10:00", "2025-06-25 11:00", "2025-06-25 12:00", "2025-06-25 13:00",
            "2025-06-25 14:00", "2025-06-25 15:00", "2025-06-25 16:00", "2025-06-25 21:00", "2025-06-25 23:00"
        ]),
        "air_humidity": [78, 75, 60, 70, 65, 75, 72, 68, 66, 70, 74, 65, 62]
    }
    df = pd.DataFrame(data)
else:
    pot_id = os.getenv("POT_ID", "1")
    url = f"http://localhost:5000/api/air-humidity?pot_id={pot_id}"
    response = requests.get(url)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    df["created"] = pd.to_datetime(df["created"])

# Diagramm erstellen
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["created"],
    y=df["air_humidity"],
    mode='lines',
    fill='tozeroy',
    fillcolor='rgba(0, 0, 255, 0.2)',
    line=dict(color='blue', width=4),
))

fig.update_layout(
    xaxis=dict(
        title="Zeit",
        tickformat="%H:%M",
        automargin=True,
        range=["2025-06-25 06:00", "2025-06-25 23:00"],
        nticks=6
    ),
    yaxis=dict(
        title="Luftfeuchtigkeit (%)",
        showgrid=True,
        gridcolor="lightgrey",
        gridwidth=1,
        range=[20, 100]
    ),
    title_x=None,
    plot_bgcolor="white",
    font=dict(family="Arial", size=14),
    margin=dict(l=40, r=20, t=40, b=40),
)

# HTML-Datei speichern
fig.write_html("diagramme/luftfeuchtigkeit_verlauf.html", include_plotlyjs='cdn', config=dict(displayModeBar=False))