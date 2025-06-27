from flask import Blueprint, current_app, Response, request
import plotly.graph_objects as go
import pandas as pd
import requests

def fetch_plot_data(url: str, column_map: dict) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    df["created"] = pd.to_datetime(df["created"])
    for new_col, old_col in column_map.items():
        df[new_col] = df[old_col]
    return df

plots_blueprint = Blueprint('plots', __name__)

from routes.plots.temperatur_verlauf import generate_temperatur_plot
from routes.plots.bodenfeuchtigkeit_verlauf import generate_bodenfeuchtigkeit_plot
from routes.plots.luftfeuchtigkeit_verlauf import generate_luftfeuchtigkeit_plot
from routes.plots.sonnenstunden import generate_sonnenstunden_plot

def create_plot_route(plot_func, endpoint_name):
    def route():
        pot_id = request.args.get("pot_id", default=1, type=int)
        html = plot_func(pot_id)
        return Response(html, mimetype="text/html")
    route.__name__ = endpoint_name
    return route

plots_blueprint.add_url_rule("/plot/temperature", view_func=create_plot_route(generate_temperatur_plot, "plot_temperature"))
plots_blueprint.add_url_rule("/plot/luftfeuchtigkeit", view_func=create_plot_route(generate_luftfeuchtigkeit_plot, "plot_luftfeuchtigkeit"))
plots_blueprint.add_url_rule("/plot/soil", view_func=create_plot_route(generate_bodenfeuchtigkeit_plot, "plot_soil"))
plots_blueprint.add_url_rule("/plot/sunlight", view_func=create_plot_route(generate_sonnenstunden_plot, "plot_sunlight"))
