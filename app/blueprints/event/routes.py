from flask import render_template, redirect, abort, url_for
from flask_login import login_required, current_user
from app.models.event import Event
from . import event


@event.route('/')
@login_required
def events_view():
    return render_template('event/event.html', user_name=current_user.user_name)


@event.route('/add_event', methods=['GET'])
@login_required
def add_event():

    return render_template('event/add_event.html')


@event.route('/update/<int:event_id>')
@login_required
def update_event_form(event_id):
    # Assuming you have authentication in place
    if not current_user.is_authenticated:
        return redirect(url_for('login'))  # Redirect to login if the user is not authenticated

    # Retrieve the workplace data from your database
    event = Event.query.get(event_id)
    if event is None:
        abort(404)  # Workplace not found

    # Check if the current user is authorized to edit this workplace
    if current_user.id != event.user_id:
        abort(403)  # Unauthorized access

    # Render the update template with the workplace data
    return render_template('event/update_event.html', event=event, user_name=current_user.user_name)