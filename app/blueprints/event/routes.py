from flask import render_template, abort, redirect, url_for
from flask_login import login_required, current_user
from app.models.event import Event
from . import event


@event.route('/')
@login_required
def events_view():
    return render_template('event/event.html', user_name=current_user.user_name)

