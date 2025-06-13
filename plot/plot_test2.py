

import plotly.express as px
import pandas as pd

# Beispiel-Daten erstellen
data = [
    {"date": "2025-05-01", "HoS": 6},
    {"date": "2025-05-02", "HoS": 8},
    {"date": "2025-05-03", "HoS": 7},
    {"date": "2025-05-04", "HoS": 5},
    {"date": "2025-05-05", "HoS": 9}
]

# DataFrame erstellen
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

# Diagramm erzeugen
fig = px.bar(
    df,
    x="date",
    y="HoS",
    title="Sonnenstunden der letzten 30 Tage (Testdaten)",
    labels={"date": "Datum", "HoS": "Sonnenstunden"}
)

# Als HTML speichern
fig.write_html("diagramme/test_sonnenstunden.html")
print("Diagramm erfolgreich erstellt: diagramme/test_sonnenstunden.html")