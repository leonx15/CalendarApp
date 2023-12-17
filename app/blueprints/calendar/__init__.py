# In app/blueprints/workplaces/__init__.py
from flask import Blueprint
calendar = Blueprint('calendar', __name__)
from . import routes