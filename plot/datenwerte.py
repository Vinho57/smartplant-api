

import plotly.graph_objects as go
import pandas as pd
import requests

# Daten von der API holen
response = requests.get("http://localhost:5000/average-month")
data = response.json()

# Nur ein Eintrag wird erwartet, daher direkt nutzen
d = data[0]

# Werte extrahieren
labels = ["Temperatur (°C)", "Bodenfeuchtigkeit (%)", "Luftfeuchtigkeit (%)", "Sonnenstunden"]
values = [d["temperature"], d["ground_humidity"], d["air_humidity"], d["HoS"]]

# Balkendiagramm erstellen
fig = go.Figure([go.Bar(x=labels, y=values)])
fig.update_layout(title="Durchschnittswerte im aktuellen Monat")

# HTML speichern
fig.write_html("diagramme/datenwerte.html")