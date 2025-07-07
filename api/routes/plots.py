from flask import Blueprint, Response, request
from routes.api_handler import APIHandler
from routes.plot_configs import PLOT_CONFIGS
from routes.plot_generator import PlotGenerator


from routes.plot_generator import PlotGenerator

plots_blueprint = Blueprint('plots', __name__)

api_handler = APIHandler("http://localhost:5001")

@plots_blueprint.route("/plots/<plot_type>", methods=["GET"])
def render_dynamic_plot(plot_type):
    pot_id = int(request.args.get("pot_id", 1))

    if plot_type not in PLOT_CONFIGS:
        return Response("Ungültiger Plot-Typ", status=404)

    endpoint = PLOT_CONFIGS[plot_type]["endpoint"]
    df = api_handler.get_df(pot_id, endpoint)
    config = PLOT_CONFIGS[plot_type]["config"](df)

    html = PlotGenerator(df).generate(**config)
    return Response(html, mimetype="text/html")