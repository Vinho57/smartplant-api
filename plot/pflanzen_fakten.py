import os
import requests
import plotly.graph_objects as go

pot_id = os.getenv("POT_ID", "1")

USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

if USE_DUMMY:
    d = {
        "pot_id": 1,
        "temperature": 23.5,
        "ground_humidity": 64,
        "air_humidity": 58,
        "sunlight": 13500,
        "created": "2025-06-25 14:30"
    }
else:
    url = f"http://localhost:5000/latest-today?pot_id={pot_id}"
    response = requests.get(url)
    response.raise_for_status()
    d = response.json()[0]

# Tabelle vorbereiten
header = ["Eigenschaft", "Wert"]
values = [
    ["Topf-ID", "Temperatur (°C)", "Bodenfeuchtigkeit (%)", "Luftfeuchtigkeit (%)", "Sonnenlicht (Lux)", "Zeitpunkt"],
    [d["pot_id"], d["temperature"], d["ground_humidity"], d.get("air_humidity"), d.get("sunlight"), d["created"]]
]

# Tabelle als Grafik anzeigen
fig = go.Figure(data=[go.Table(
    header=dict(values=header, fill_color='paleturquoise', align='left'),
    cells=dict(values=values, fill_color='lavender', align='left'))
])

fig.update_layout(
    width=600
)

# HTML speichern
fig.write_html("diagramme/pflanzen_fakten.html", config=dict(displayModeBar=False))