import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_temperatur_plot(df=None, use_dummy=True):
    if use_dummy or df is None:
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
        df = pd.DataFrame(data)
        df["created"] = pd.to_datetime(df["created"])

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

    layout = get_standard_layout(
        x_title="Zeit",
        y_title="Temperatur (°C)",
        y_range=[df["temperature"].min() - 1, df["temperature"].max() + 1],
        x_range=[
            str(df["created"].min().replace(hour=0, minute=0)),
            str(df["created"].max().replace(hour=23, minute=59))
        ]
    )
    fig.update_layout(layout)

    return fig.to_html(include_plotlyjs='cdn', config=dict(displayModeBar=False))
