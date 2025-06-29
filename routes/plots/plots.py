from flask import Blueprint, Response, request
from routes.plots.api_handler import ApiHandler

from routes.plots.temperatur_verlauf import generate_temperatur_plot
from routes.plots.bodenfeuchtigkeit_verlauf import generate_bodenfeuchtigkeit_plot
from routes.plots.luftfeuchtigkeit_verlauf import generate_luftfeuchtigkeit_plot
from routes.plots.sonnenstunden import generate_sonnenstunden_plot

plots_blueprint = Blueprint('plots', __name__)

api_handler = ApiHandler("http://localhost:5001")

def render_plot(generate_plot_func, df):
    return Response(generate_plot_func(df=df), mimetype='text/html')


@plots_blueprint.route("/plots/temperature", methods=["GET"])
def render_temperature_plot():
    pot_id = int(request.args.get("pot_id", 1))
    df = api_handler.get_data("latest-today", pot_id)
    return Response(generate_temperatur_plot(df), mimetype="text/html")

@plots_blueprint.route("/plots/soil", methods=["GET"])
def render_soil_plot():
    pot_id = int(request.args.get("pot_id", 1))
    df = api_handler.get_data("latest-today", pot_id)
    return Response(generate_bodenfeuchtigkeit_plot(df), mimetype="text/html")

@plots_blueprint.route("/plots/luftfeuchtigkeit", methods=["GET"])
def render_luftfeuchtigkeit_plot():
    pot_id = int(request.args.get("pot_id", 1))
    df = api_handler.get_data("latest-today", pot_id)
    return Response(generate_luftfeuchtigkeit_plot(df), mimetype="text/html")

@plots_blueprint.route("/plots/sunlight", methods=["GET"])
def render_sunlight_plot():
    pot_id = int(request.args.get("pot_id", 1))
    df = api_handler.get_data("sunlight-30days", pot_id)
    return Response(generate_sonnenstunden_plot(df), mimetype="text/html")
