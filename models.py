from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    birth_date = db.Column(db.Date)
