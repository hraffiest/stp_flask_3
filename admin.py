from flask import Flask
from config import Config
from models import *
from __init__ import app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(app)


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


admin.add_view(NewModel(Location, db.session))
admin.add_view(NewModel(Enrollment, db.session))
admin.add_view(NewModel(Participant, db.session))
admin.add_view(NewModel(Event, db.session))