

import plotly.graph_objects as go
import requests

# Daten abrufen
response = requests.get("http://localhost:5000/latest-today")
data = response.json()

# Nur den ersten Eintrag verwenden (aktueller Zustand)
d = data[0]

# Tabelle vorbereiten
header = ["Topf-ID", "Temperatur (°C)", "Bodenfeuchtigkeit (%)", "Luftfeuchtigkeit (%)", "Zeitpunkt"]
values = [[d["pot_id"]], [d["temperature"]], [d["ground_humidity"]], [d["air_humidity"]], [d["created"]]]

# Tabelle als Grafik anzeigen
fig = go.Figure(data=[go.Table(
    header=dict(values=header, fill_color='paleturquoise', align='left'),
    cells=dict(values=values, fill_color='lavender', align='left'))
])

fig.update_layout(title="Aktuelle Pflanzenfakten")

# HTML speichern
fig.write_html("diagramme/pflanzen_fakten.html")