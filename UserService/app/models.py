from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    date_of_registration = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    country = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)