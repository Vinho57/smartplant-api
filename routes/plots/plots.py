from flask import Blueprint, Response, request
from routes.plots.api_handler import ApiHandler

from routes.plots.temperatur_verlauf import generate_temperatur_plot
from routes.plots.bodenfeuchtigkeit_verlauf import generate_bodenfeuchtigkeit_plot
from routes.plots.luftfeuchtigkeit_verlauf import generate_luftfeuchtigkeit_plot
from routes.plots.sonnenstunden import generate_sonnenstunden_plot

plots_blueprint = Blueprint('plots', __name__)

def render_plot(generate_plot_func, df):
    return Response(generate_plot_func(df=df), mimetype='text/html')

def handle_plot(pot_id, plot_func, use_sunlight=False):
    api = ApiHandler("http://localhost:5001", pot_id)
    df = api.get_sunlight_df() if use_sunlight else api.get_df()
    return render_plot(plot_func, df)

@plots_blueprint.route("/plots/temperature", methods=["GET"])
def render_temperature_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return handle_plot(pot_id, generate_temperatur_plot)

@plots_blueprint.route("/plots/soil", methods=["GET"])
def render_soil_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return handle_plot(pot_id, generate_bodenfeuchtigkeit_plot)

@plots_blueprint.route("/plots/luftfeuchtigkeit", methods=["GET"])
def render_luftfeuchtigkeit_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return handle_plot(pot_id, generate_luftfeuchtigkeit_plot)

@plots_blueprint.route("/plots/sunlight", methods=["GET"])
def render_sunlight_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return handle_plot(pot_id, generate_sonnenstunden_plot, use_sunlight=True)
