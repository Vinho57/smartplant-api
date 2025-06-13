

import plotly.express as px
import pandas as pd
import requests

# API-Daten abrufen
response = requests.get("http://localhost:5000/all-today")
data = response.json()

# In DataFrame umwandeln
df = pd.DataFrame(data)
df['created'] = pd.to_datetime(df['created'])

# Diagramm erstellen
fig = px.line(
    df,
    x="created",
    y="air_humidity",
    title="Luftfeuchtigkeitsverlauf",
    labels={"created": "Uhrzeit", "air_humidity": "Luftfeuchtigkeit (%)"}
)

# HTML-Datei speichern
fig.write_html("diagramme/luftfeuchtigkeit_verlauf.html")