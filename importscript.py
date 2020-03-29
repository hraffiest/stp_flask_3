import csv
from __init__ import app
from config import Config
from models import *


with open('meetup_events.csv', 'r') as data:
    events_csv = csv.reader(data)
    events = list(events_csv)

    for row in events[1:]:
        loc = db.session.query(Location).filter(Location.code == row[6]).first()
        event = Event(title=row[0],
                      description=row[1],
                      date=row[2],
                      time=row[3],
                      category=row[4],
                      type=row[5],
                      location=loc,
                      adress=row[7],
                      seats=row[8],
                      )
        with app.app_context():
            db.session.add(event)

# import works only with commit in cycle 'for'. Why?
with app.app_context():
    db.session.commit()