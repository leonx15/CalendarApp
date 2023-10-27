from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Importuj ustawienia konfiguracyjne
from config import Config

# Inicjalizacja aplikacji
app = Flask(__name__)
app.config.from_object(Config)  # Załaduj ustawienia konfiguracyjne

# Inicjalizacja rozszerzeń
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Importuj routy
from auth import *
from main import *

if __name__ == '__main__':
    app.run(debug=True)
