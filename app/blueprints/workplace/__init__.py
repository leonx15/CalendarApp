# In app/blueprints/workplaces/__init__.py
from flask import Blueprint
workplaces = Blueprint('workplaces', __name__)
from . import routes