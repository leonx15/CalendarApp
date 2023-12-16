from app import app
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.secure_area'))
    return redirect(url_for('auth.login'))


@app.route('/secure_area')
@login_required
def secure_area():
    return render_template('main/secure_area.html', user_name=current_user.user_name)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', user_name=current_user.user_name)

