from app import db
from flask_login import current_user

class Workplace(db.Model):
    __tablename__ = 'workplaces'  # Optional: specify a custom table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    house_number = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    nip_number = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Additional fields can be added here

    def __repr__(self):
        return f'<Workplace {self.name}>'
