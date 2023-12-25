from flask import render_template, abort, redirect, url_for
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

@workplaces.route('/update/<int:workplace_id>')
@login_required
def update_workplace_form(workplace_id):
    # Assuming you have authentication in place
    if not current_user.is_authenticated:
        return redirect(url_for('login'))  # Redirect to login if the user is not authenticated

    # Retrieve the workplace data from your database
    workplace = Workplace.query.get(workplace_id)
    if workplace is None:
        abort(404)  # Workplace not found

    # Check if the current user is authorized to edit this workplace
    if current_user.id != workplace.user_id:
        abort(403)  # Unauthorized access

    # Render the update template with the workplace data
    return render_template('workplace/update_workplace.html', workplace=workplace, user_name=current_user.id)