from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app import app, db
from forms import WorkplaceForm, EventForm, ManageUserForm
from models import Workplace, Event, User
from utils import requires_role
import json

@app.route('/dashboard/')
@login_required
def dashboard():
    workplaces = current_user.workplaces
    return render_template('dashboard.html', name=current_user.username, workplaces=workplaces)

@app.route('/add_workplace/', methods=['GET', 'POST'])
@login_required
def add_workplace():
    form = WorkplaceForm()
    if form.validate_on_submit():
        workplace = Workplace(name=form.name.data, address=form.address.data, owner=current_user)
        db.session.add(workplace)
        db.session.commit()
        flash('Dodano nowe miejsce pracy!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_workplace.html', form=form)

@app.route('/delete_workplace/<int:workplace_id>', methods=['POST'])
@login_required
def delete_workplace(workplace_id):
    workplace = Workplace.query.get_or_404(workplace_id)
    if workplace.owner != current_user:
        abort(403)  # Forbidden, user does not own this workplace
    db.session.delete(workplace)
    db.session.commit()
    flash('Miejsce pracy zostało usunięte.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/calendar')
@login_required
def calendar():
    events = Event.query.filter_by(user_id=current_user.id).all()
    return render_template('calendar.html', events=events)


@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(start_time=form.start_time.data, end_time=form.end_time.data, Workplace=form.workplace.data, user=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Dyżur został dodany!', 'success')
        return redirect(url_for('calendar'))
    return render_template('add_event.html', form=form)


@app.route('/fetch_events')
@login_required
def fetch_events():
    events = Event.query.filter_by(user_id=current_user.id).all()
    events_data = [
        {
            'id': event.id,
            'title': 'Dyżur w ' + event.Workplace.name,
            'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S')
        }
        for event in events
    ]
    return json.dumps(events_data)

@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)

    # Upewnij się, że użytkownik ma prawo edytować to wydarzenie
    if event.user_id != current_user.id:
        flash('NIe masz uprawnień do zmain w tym dyżurze.', 'danger')
        return redirect(url_for('dashboard'))

    form = EventForm(obj=event)  # Wypełnij formularz danymi z wydarzenia

    if form.validate_on_submit():
        form.populate_obj(event)  # Aktualizuj obiekt wydarzenia danymi z formularza
        db.session.commit()
        flash('Dyżur został zaktualizowany.', 'success')
        return redirect(url_for('calendar'))

    return render_template('edit_event.html', form=form, event=event)


@app.route('/delete_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user_id != current_user.id:  # upewnij się, że tylko właściciel może usunąć wydarzenie
        abort(403)
    db.session.delete(event)
    db.session.commit()
    flash('Wydarzenie zostało usunięte.', 'success')
    return redirect(url_for('calendar'))


@app.route('/manage_users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if current_user.role != "Admin":
        return redirect(url_for('dashboard'))

    users = User.query.all()
    return render_template('manage_users.html', users=users, form=ManageUserForm())


@app.route('/change_user_role/<int:user_id>', methods=['POST'])
@login_required
@requires_role('Admin')
def change_user_role(user_id):
    form = ManageUserForm()
    user = User.query.get(user_id)
    if user and form.validate_on_submit():
        user.role = form.role.data
        db.session.commit()
        flash('Role changed successfully.', 'success')
    return redirect(url_for('manage_users'))
