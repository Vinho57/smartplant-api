from flask import Blueprint, Response, request
from routes.plots.plot_utils import (
    get_all_measurements_for_today,
    get_sunlight_last_30_days
)

from routes.plots.temperatur_verlauf import generate_temperatur_plot
from routes.plots.bodenfeuchtigkeit_verlauf import generate_bodenfeuchtigkeit_plot
from routes.plots.luftfeuchtigkeit_verlauf import generate_luftfeuchtigkeit_plot
from routes.plots.sonnenstunden import generate_sonnenstunden_plot

plots_blueprint = Blueprint('plots', __name__)


def render_plot(generate_plot_func, pot_id):
    df = get_all_measurements_for_today(pot_id)
    return Response(generate_plot_func(df=df, use_dummy=False), mimetype='text/html')


@plots_blueprint.route("/plots/temperature", methods=["GET"])
def render_temperature_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return render_plot(generate_temperatur_plot, pot_id)

@plots_blueprint.route("/plots/soil", methods=["GET"])
def render_soil_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return render_plot(generate_bodenfeuchtigkeit_plot, pot_id)

@plots_blueprint.route("/plots/luftfeuchtigkeit", methods=["GET"])
def render_luftfeuchtigkeit_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return render_plot(generate_luftfeuchtigkeit_plot, pot_id)

@plots_blueprint.route("/plots/sunlight", methods=["GET"])
def render_sunlight_plot():
    pot_id = int(request.args.get("pot_id", 1))
    return render_plot(generate_sonnenstunden_plot, pot_id)
