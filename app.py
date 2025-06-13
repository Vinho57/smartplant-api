import os
from flask import Flask
from routes.views import views_blueprint
from routes.users import users_blueprint
from routes.plants import plants_blueprint
from routes.authorization import authorization_blueprint

app = Flask(__name__)

# Datenbank-Konfiguration zentral definieren
app.config['DB_CONFIG'] = {
    "host": "192.168.178.162",
    "user": "admin",
    "password": "thws2025",
    "database": "smartplantpot"
}

# Blueprint für View-Routen registrieren
app.register_blueprint(views_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(plants_blueprint)
app.register_blueprint(authorization_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)