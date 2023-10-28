from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import app, db
from forms import RegisterForm, LoginForm
from models import User
from utils import hash_password

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password, salt = hash_password(form.password.data)
        user = User(username=form.username.data, password=hashed_password, salt=salt)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            hashed_password, _ = hash_password(form.password.data, user.salt)
            if hashed_password == user.password:
                if user.role == "Guest":
                    flash('Your account is in Guest mode and cannot be used to log in.', 'danger')
                else:
                    login_user(user)
                    return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials')
        else:
            flash('Invalid credentials')
    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
