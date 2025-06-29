import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_bodenfeuchtigkeit_plot(df=None, use_dummy=True):
    if use_dummy or df is None:
        # Dummy-Daten verwenden
        data = {
            "created": pd.to_datetime([
                "2025-06-25 06:00", "2025-06-25 07:00", "2025-06-25 08:00", "2025-06-25 09:00",
                "2025-06-25 10:00", "2025-06-25 11:00", "2025-06-25 12:00", "2025-06-25 13:00",
                "2025-06-25 14:00", "2025-06-25 15:00", "2025-06-25 16:00", "2025-06-25 21:00", "2025-06-25 23:00"
            ]),
            "soil_moisture": [40, 42, 43, 45, 44, 46, 47, 49, 48, 46, 45, 43, 42]
        }
        df = pd.DataFrame(data)

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
