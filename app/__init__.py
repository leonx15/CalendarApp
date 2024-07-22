from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the Flask application
app = Flask(__name__)

# Application Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize Extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Import models
from app.models.user import User  # Assuming you have a user model in the models directory

# Import and register Blueprints
from app.blueprints.auth import auth as auth_blueprint
from app.blueprints.main import main as main_blueprint
from app.blueprints.calendar import calendar as calendar_blueprint
from app.blueprints.api import api as api_blueprint
from app.blueprints.workplace import workplaces as workplaces_blueprint

# Some changes are made
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(calendar_blueprint, url_prefix='/calendar')
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(workplaces_blueprint, url_prefix='/workplace')


# Setup the login manager user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
