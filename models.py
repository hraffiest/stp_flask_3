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
    address = db.Column(db.String, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    loc_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    location = db.relationship('Location', back_populates="events")
    participants = db.relationship('Participant', back_populates="events")
    enrollments = db.relationship('Enrollment', back_populates="event")


class Participant(db.Model):
    __tablename__ = 'participants'
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    location = db.Column(db.String)
    enrollments = db.relationship('Enrollment', back_populates="participant")
    events = db.relationship('Event', back_populates="participants")
    about = db.Column(db.String)


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    event = db.relationship('Event', back_populates="enrollments")
    part_id = db.Column(db.Integer, db.ForeignKey("participants.id"))
    participant = db.relationship('Participant', back_populates="enrollments")
    datetime = db.Column(db.DateTime, nullable=False)


class Location(db.Model):
    __tablename__ = 'locations'
    events = db.relationship('Event', back_populates="location")
    title = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)