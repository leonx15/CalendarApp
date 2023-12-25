from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.workplace import Workplace

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Optional: specify a custom table name

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    event = db.relationship('Event', backref='event', lazy='dynamic')
    workplace = db.relationship('Workplace', backref='user', lazy='dynamic')

    # Additional fields can be added here

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
