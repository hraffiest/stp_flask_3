from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'events'
    e_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    location = db.relationship('Location')
    address = db.Column(db.String, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    participants = db.relationship('Participant', back_populates="events")


class Participant(db.Model):
    __tablename__ = 'participants'
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    location = db.Column(db.String)
    enrollments = db.relationship('Enrollment', back_populates="participant")
    about = db.Column(db.String)


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    event = db.relationship('Event')
    participant = db.relationship('Participant', back_populates="enrollments")


class Location(db.Model):
    __tablename__ = 'locations'
    title = db.Column(db.String)
    code = db.Column(db.String)