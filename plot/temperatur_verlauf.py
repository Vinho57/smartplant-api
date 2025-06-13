

import plotly.express as px
import pandas as pd

# Testdaten manuell definieren
data = [
    {"created": "2025-06-08 08:00:00", "temperature": 22.1},
    {"created": "2025-06-08 10:00:00", "temperature": 23.5},
    {"created": "2025-06-08 12:00:00", "temperature": 24.8},
    {"created": "2025-06-08 14:00:00", "temperature": 25.2},
    {"created": "2025-06-08 16:00:00", "temperature": 23.9}
]

# In DataFrame umwandeln
df = pd.DataFrame(data)
df['created'] = pd.to_datetime(df['created'])

# Diagramm erstellen
fig = px.line(df, x="created", y="temperature", title="Temperaturverlauf", labels={"created": "Uhrzeit", "temperature": "Temperatur (°C)"})

# HTML-Datei speichern
fig.write_html("temperatur_verlauf.html")