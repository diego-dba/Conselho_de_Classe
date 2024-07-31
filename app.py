from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

import routes
import models

with app.app_context():
    db.create_all()
