from flask import Flask, jsonify
from flask_login import login_required, current_user
from . import api

@api.route('/events')
def get_events():
    # Fetch or generate event data
    events = [
        {'title': 'Event 1', 'start': '2023-12-01'},
        {'title': 'Event 2', 'start': '2023-12-02'}
    ]
    return jsonify(events)




