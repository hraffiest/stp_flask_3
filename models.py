from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    date = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    type = db.Column(db.String)
    category = db.Column(db.String)
    location = db.relationship('Location', back_populates="events")
    address = db.Column(db.String)
    seats = db.Column(db.Integer)
    participants = db.relationship('Participant', back_populates="events")


