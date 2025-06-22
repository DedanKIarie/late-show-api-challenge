from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<USERR>:<PASS>@localhost:5432/late_show_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)