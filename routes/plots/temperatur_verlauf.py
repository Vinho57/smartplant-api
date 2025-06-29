import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_temperatur_plot(df):
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
