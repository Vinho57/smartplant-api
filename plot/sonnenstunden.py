import os
import requests
import plotly.graph_objects as go
import pandas as pd

USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

if USE_DUMMY:
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    sunlight = [round(max(0, 12 + 4 * (0.5 - i % 3))) for i in range(30)]  # Beispielwerte
    df = pd.DataFrame({"created": dates, "sunlight": sunlight})
else:
    pot_id = os.getenv("POT_ID", "1")
    url = f"http://localhost:5000/sunlight-30days?pot_id={pot_id}"
    response = requests.get(url)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    df["created"] = pd.to_datetime(df["created"])

fig = go.Figure()
fig.add_trace(go.Bar(
    x=df["created"],
    y=df["sunlight"],
    marker_color='orange'
))

fig.update_layout(
    xaxis=dict(
        title="Datum",
        tickformat="%d.%m",
        tickangle=45,
        automargin=True
    ),
    yaxis=dict(
        title="Sonnenstunden",
        showgrid=True,
        gridcolor="lightgrey"
    ),
    plot_bgcolor="white",
    font=dict(family="Arial", size=14),
    margin=dict(l=40, r=20, t=40, b=80),
)

fig.write_html("diagramme/sonnenstunden_verlauf.html", include_plotlyjs='cdn', config=dict(displayModeBar=False))