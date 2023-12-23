from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from . import workplaces


@workplaces.route('/')
@login_required
def workplaces_view():
    return render_template('workplace/workplace.html', user_name=current_user.user_name)


@workplaces.route('/add_workplace', methods=['GET', 'POST'])
@login_required
def add_workplace():

    return render_template('workplace/add_workplace.html')
