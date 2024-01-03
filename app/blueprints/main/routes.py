from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from . import main


@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('main/secure_area.html', user_name=current_user.user_name)
    else:
        return redirect(url_for('auth.login'))


@main.route('/secure_area')
@login_required
def secure_area():
    return render_template('main/secure_area.html', user_name=current_user.user_name)


@main.route('/dashboard')
@login_required
def dashboard():
    now = datetime.now()
    return render_template('main/dashboard.html', user_name=current_user.user_name, now=now)
