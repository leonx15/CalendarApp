from flask import jsonify, request, abort
from flask_login import login_required, current_user
from . import api
from app import db
from app.models.worplace import Workplace


@api.route('/events')
@login_required
def get_events():
    # Fetch or generate event data
    events = [
        {'title': 'Event 1', 'start': '2023-12-01'},
        {'title': 'Event 2', 'start': '2023-12-02'}
    ]
    return jsonify(events)


@api.route('/workplaces', methods=['GET'])
@login_required
def get_workplaces():
    # Fetch or generate event data
    user_workplaces = Workplace.query.filter_by(user_id=current_user.id).all()
    workplaces_data = [workplace.to_dict() for workplace in user_workplaces]
    return jsonify(workplaces_data)


@api.route('/add_workplace', methods=['POST'])
@login_required
def create_workplace():
    if not request.json:
        abort(400, description="Not a JSON request")

    # Assuming the JSON contains all the necessary workplace fields
    name = request.json.get('name')
    street = request.json.get('street')
    house_number = request.json.get('house_number')
    zip_code = request.json.get('zip_code')
    city = request.json.get('city')
    nip_number = request.json.get('nip_number')
    user_id = current_user.id

    # Validate received data as needed

    new_workplace = Workplace(
        name=name,
        street=street,
        house_number=house_number,
        zip_code=zip_code,
        city=city,
        nip_number=nip_number,
        user_id=user_id
    )

    db.session.add(new_workplace)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

    return jsonify(new_workplace.to_dict()), 201
