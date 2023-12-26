from app import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'  # Optional: specify a custom table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplaces.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Additional fields can be added here

    def __repr__(self):
        return f'<Event {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'workplace_id': self.workplace_id,
            'user_id': self.user_id
        }

    def calendar_data(self):
        return {
            'title': self.name,
            'start': self.start_date.isoformat(),
            'end': self.end_date.isoformat()
        }