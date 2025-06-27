import os
import pandas as pd
import plotly.graph_objects as go
from routes.plots.plots import fetch_plot_data

def generate_temperatur_plot(pot_id: int) -> str:
    USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

    if USE_DUMMY:
        data = [
            {"created": "2025-06-22 08:00:00", "temperature": 21.3},
            {"created": "2025-06-22 09:00:00", "temperature": 21.5},
            {"created": "2025-06-22 10:00:00", "temperature": 22.8},
            {"created": "2025-06-22 11:00:00", "temperature": 23.2},
            {"created": "2025-06-22 12:00:00", "temperature": 24.1},
            {"created": "2025-06-22 13:00:00", "temperature": 24.7},
            {"created": "2025-06-22 14:00:00", "temperature": 25.0},
            {"created": "2025-06-22 15:00:00", "temperature": 24.3},
            {"created": "2025-06-22 16:00:00", "temperature": 25.7},
            {"created": "2025-06-22 17:00:00", "temperature": 22.9},
            {"created": "2025-06-22 18:00:00", "temperature": 22.1},
            {"created": "2025-06-22 19:00:00", "temperature": 21.5}
        ]
    else:
        url = f"http://localhost:5000/latest-today?pot_id={pot_id}"
        data = fetch_plot_data(url, {"temperature": "temperature"})

    df = pd.DataFrame(data)
    df['created'] = pd.to_datetime(df['created'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['created'],
        y=df['temperature'],
        mode='lines',
        fill='tozeroy',
        fillcolor='rgba(255, 0, 0, 0.15)',
        line=dict(color='red', width=4.5),
        hoverinfo='x+y',
        name='Temperatur'
    ))

    fig.update_layout(
        title_x=None,
        xaxis=dict(
            title="Zeit",
            tickformat="%H:%M",
            dtick=3600000.0,
            showgrid=False,
            tickmode="auto"
        ),
        yaxis=dict(
            title="Temperatur (°C)",
            ticksuffix=" °C",
            showgrid=True,
            gridcolor="lightgrey",
            range=[15, 26]
        ),
        plot_bgcolor="white",
        font=dict(family="Arial", size=14),
        margin=dict(l=40, r=20, t=60, b=40),
        modebar=dict(remove=["zoom", "pan", "select", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "resetScale2d"]),
        showlegend=False,
        dragmode=False,
    )

    return fig.to_html(include_plotlyjs='cdn', config=dict(displayModeBar=False))