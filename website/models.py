from . import db  # importing databse from __init__.py file
from flask_login import UserMixin
from sqlalchemy.sql import func # give current datetime 

class UserData(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('UserNotes')

class UserNotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    refrence_key = db.Column(db.Integer, db.ForeignKey('user_data.id'))
