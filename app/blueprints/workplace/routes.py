from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import workplaces


@workplaces.route('/')
def workplaces_view():
    return render_template('workplace/workplace.html', user_name=current_user.user_name)
