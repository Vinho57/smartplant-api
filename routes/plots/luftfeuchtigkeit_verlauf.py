import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_luftfeuchtigkeit_plot(df=None, use_dummy=False):
    if use_dummy or df is None:
        data = {
            "created": pd.to_datetime([
                "2025-06-25 06:00", "2025-06-25 07:00", "2025-06-25 08:00", "2025-06-25 09:00",
                "2025-06-25 10:00", "2025-06-25 11:00", "2025-06-25 12:00", "2025-06-25 13:00",
                "2025-06-25 14:00", "2025-06-25 15:00", "2025-06-25 16:00", "2025-06-25 21:00", "2025-06-25 23:00"
            ]),
            "luftfeuchtigkeit": [78, 75, 60, 70, 65, 75, 72, 68, 66, 70, 74, 65, 62]
        }
        df = pd.DataFrame(data)

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
