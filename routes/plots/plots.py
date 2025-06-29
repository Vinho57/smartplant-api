from flask import Blueprint, Response, request
from routes.plots.api_handler import ApiHandler

from routes.plots.temperatur_verlauf import generate_temperatur_plot
from routes.plots.bodenfeuchtigkeit_verlauf import generate_bodenfeuchtigkeit_plot
from routes.plots.luftfeuchtigkeit_verlauf import generate_luftfeuchtigkeit_plot
from routes.plots.sonnenstunden import generate_sonnenstunden_plot

plots_blueprint = Blueprint('plots', __name__)

def render_plot(generate_plot_func, df):
    return Response(generate_plot_func(df=df), mimetype='text/html')

@plots_blueprint.route("/plots/all", methods=["GET"])
def render_all_plots():
    pot_id = int(request.args.get("pot_id", 1))
    api = ApiHandler("http://localhost:5001", pot_id)

    df = api.get_latest_df()
    df_sunlight = api.get_sunlight_df()

    html_temp = generate_temperatur_plot(df)
    html_soil = generate_bodenfeuchtigkeit_plot(df)
    html_air = generate_luftfeuchtigkeit_plot(df)
    html_sun = generate_sonnenstunden_plot(df_sunlight)

    html = f"""
    <html><body>
        <h2>Temperatur</h2>{html_temp}
        <h2>Bodenfeuchtigkeit</h2>{html_soil}
        <h2>Luftfeuchtigkeit</h2>{html_air}
        <h2>Sonnenstunden</h2>{html_sun}
    </body></html>
    """

    return Response(html, mimetype='text/html')
