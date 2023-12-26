from flask import render_template
from flask_login import login_required, current_user
from . import event


@event.route('/')
@login_required
def events_view():
    return render_template('event/event.html', user_name=current_user.user_name)


@event.route('/add_event', methods=['GET'])
@login_required
def add_event():

    return render_template('event/add_event.html')
