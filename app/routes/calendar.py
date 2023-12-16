from app import app
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


@app.route('/')
@login_required
def calendarview():
    return render_template('calendar/calendar.html', user_name=current_user.user_name)


