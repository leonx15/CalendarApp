import hashlib
import os
from models import User
from app import login_manager
from functools import wraps
from flask_login import current_user
from flask import request, redirect, url_for, flash

def hash_password(password, salt=None):
    """Hash a password using a given salt or generate a new salt if none provided."""
    if not salt:
        salt = os.urandom(16)  # generowanie losowej soli
    password_salt = password.encode('utf-8') + salt
    hashed_password = hashlib.sha256(password_salt).hexdigest()
    return hashed_password, salt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def requires_role(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role != required_role:
                flash('You do not have the required permissions to access this page.', 'danger')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator