from flask import Flask
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from views import *


