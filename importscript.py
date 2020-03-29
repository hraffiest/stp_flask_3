import csv
import datetime
from __init__ import app
from config import Config
from models import *


with app.app_context(), open('meetup_events.csv', 'r') as data:
    events_csv = csv.reader(data)
    events = list(events_csv)
    for row in events[1:]:
        loc = db.session.query(Location).filter(Location.code == row[6]).first()
        date = datetime.datetime.strptime(row[2] + row[3], '%d.%m.%Y%H:%M')
        event = Event(title=row[0],
                      description=row[1],
                      datetime=date,
                      category=row[4],
                      type=row[5],
                      location=loc,
                      address=row[7],
                      seats=row[8],
                      )
        db.session.add(event)
    db.session.commit()
