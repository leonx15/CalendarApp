from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models.user import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('main.secure_area'))
        else:
            flash('Invalid login credentials')

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            new_user = User(user_name=user_name, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('Email already registered')

    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
