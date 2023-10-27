from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app import app, db
from forms import WorkplaceForm, EventForm
from models import Workplace, Event
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
    events = Event.query.filter_by(owner_id=current_user.id).all()
    return render_template('calendar.html', events=events)


@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(start_time=form.start_time.data, end_time=form.end_time.data, location=form.location.data, user=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Event added successfully!', 'success')
        return redirect(url_for('calendar'))
    return render_template('add_event.html', form=form)


@app.route('/fetch_events')
@login_required
def fetch_events():
    events = Event.query.filter_by(owner_id=current_user.id).all()
    events_data = [
        {
            'id': event.id,
            'title': 'Dyżur w ' + event.location.name,
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
    if event.owner_id != current_user.id:
        flash('You do not have permission to edit this event.', 'danger')
        return redirect(url_for('dashboard'))

    form = EventForm(obj=event)  # Wypełnij formularz danymi z wydarzenia

    if form.validate_on_submit():
        form.populate_obj(event)  # Aktualizuj obiekt wydarzenia danymi z formularza
        db.session.commit()
        flash('Event updated successfully.', 'success')
        return redirect(url_for('calendar'))

    return render_template('edit_event.html', form=form)