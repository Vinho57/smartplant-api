import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_bodenfeuchtigkeit_plot(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["created"],
        y=df["soil_moisture"],
        mode='lines',
        fill='tozeroy',
        fillcolor='rgba(0,128,0,0.2)',
        line=dict(color='darkgreen', width=4),
    ))

    layout = get_standard_layout(
        x_title="Zeit",
        y_title="Bodenfeuchtigkeit (%)",
        y_range=[0, 100],
        x_range=["2025-06-25 00:00", "2025-06-25 23:59"]
    )
    fig.update_layout(layout)

    return fig.to_html(include_plotlyjs='cdn', config=dict(displayModeBar=False))
