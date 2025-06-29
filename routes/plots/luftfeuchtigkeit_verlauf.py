import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_luftfeuchtigkeit_plot(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["created"],
        y=df["luftfeuchtigkeit"],
        mode='lines',
        fill='tozeroy',
        fillcolor='rgba(0, 0, 255, 0.2)',
        line=dict(color='blue', width=4),
    ))

    layout = get_standard_layout(
        x_title="Zeit",
        y_title="Luftfeuchtigkeit (%)",
        y_range=[20, 100],
        x_range=["2025-06-25 00:00", "2025-06-25 23:59"]
    )
    fig.update_layout(layout)

    return fig.to_html(include_plotlyjs='cdn', config=dict(displayModeBar=False))
