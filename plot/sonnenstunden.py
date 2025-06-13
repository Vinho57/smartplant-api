

import plotly.express as px
import pandas as pd
import requests

# API-Daten abrufen
response = requests.get("http://localhost:5000/sunlight-30days")
data = response.json()

# In DataFrame umwandeln
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Diagramm erstellen
fig = px.bar(
    df,
    x="date",
    y="HoS",
    title="Sonnenstunden der letzten 30 Tage",
    labels={"date": "Datum", "HoS": "Sonnenstunden"}
)

# HTML-Datei speichern
fig.write_html("diagramme/sonnenstunden.html")