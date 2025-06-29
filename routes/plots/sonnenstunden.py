import pandas as pd
import plotly.graph_objects as go
from routes.plots.plot_utils import get_standard_layout

def generate_sonnenstunden_plot(df=None, use_dummy=False):
    if use_dummy or df is None:
        dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
        sunlight = [round(max(0, 12 + 4 * (0.5 - i % 3))) for i in range(30)]
        df = pd.DataFrame({"created": dates, "sunlight": sunlight})

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["created"],
        y=df["sunlight"],
        marker_color='orange',
        offset=0
    ))

    layout = get_standard_layout(
        x_title="Datum",
        y_title="Sonnenstunden",
        x_range=[str(df["created"].min()), str(df["created"].max())]
    )
    layout["bargap"] = 0.2
    layout["xaxis"]["tickformat"] = "%d.%m"
    fig.update_layout(layout)

    return fig.to_html(include_plotlyjs='cdn', config=dict(displayModeBar=False))
