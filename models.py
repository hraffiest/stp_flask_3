from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'events'
    e_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    datetime = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    loc_id = db.Column(db.Integer, db.ForeignKey("locations.l_id"))
    location = db.relationship('Location', back_populates="events")
    enrollments = db.relationship('Enrollment', back_populates="event")


class Participant(db.Model):
    __tablename__ = 'participants'
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    enrollments = db.relationship('Enrollment', back_populates="participant")
    about = db.Column(db.String)

    @property
    def password(self):
        # Запретим прямое обращение к паролю
        raise AttributeError("Вам не нужно знать пароль!")

    @password.setter
    def password(self, password):
        # Устанавливаем пароль через этот метод
        self._password = generate_password_hash(password)

    def password_valid(self, password):
        # Проверяем пароль через этот метод
        # Функция check_password_hash превращает password в хеш и сравнивает с хранимым
        return check_password_hash(self._password, password)


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    enrol_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.e_id"))
    event = db.relationship('Event', back_populates="enrollments")
    part_id = db.Column(db.Integer, db.ForeignKey("participants.p_id"))
    participant = db.relationship('Participant', back_populates="enrollments")
    datetime = db.Column(db.DateTime, nullable=False)


class Location(db.Model):
    __tablename__ = 'locations'
    l_id = db.Column(db.Integer, primary_key=True)
    events = db.relationship('Event', back_populates="location")
    title = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)