from flask import render_template, abort
from flask_login import login_required, current_user
from app.models.worplace import Workplace
from . import workplaces


@workplaces.route('/')
@login_required
def workplaces_view():
    return render_template('workplace/workplace.html', user_name=current_user.user_name)


@workplaces.route('/add_workplace', methods=['GET'])
@login_required
def add_workplace():

    return render_template('workplace/add_workplace.html')
