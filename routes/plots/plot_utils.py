import pandas as pd

def get_standard_layout(x_title: str, y_title: str, y_range=None, x_range=None) -> dict:
    return dict(
        xaxis=dict(
            title=x_title,
            tickformat="%H:%M",
            automargin=True,
            range=x_range if x_range is not None else ["00:00", "23:59"],
            nticks=6
        ),
        yaxis=dict(
            title=y_title,
            showgrid=True,
            gridcolor="lightgrey",
            gridwidth=1,
            range=y_range
        ),
        plot_bgcolor="white",
        font=dict(family="Arial", size=14),
        margin=dict(l=40, r=20, t=40, b=40),
    )
