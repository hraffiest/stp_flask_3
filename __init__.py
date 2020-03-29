from flask import Flask
from config import Config
from models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
admin = Admin(app)


class NewModel(ModelView):
    can_create = True
    can_edit = True
    can_delete = False


admin.add_view(NewModel(Location, db.session))
admin.add_view(NewModel(Enrollment, db.session))
admin.add_view(NewModel(Participant, db.session))
admin.add_view(NewModel(Event, db.session))

from views import *

with app.app_context():
    db.create_all()
