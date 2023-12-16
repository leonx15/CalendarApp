from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.secure_area'))
    return redirect(url_for('auth.login'))

@main.route('/secure_area')
@login_required
def secure_area():
    return render_template('secure_area.html', user_name=current_user.user_name)
