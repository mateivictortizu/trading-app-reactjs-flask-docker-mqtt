from datetime import datetime

from app import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    date_of_registration = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    country = db.Column(db.String(3), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="USER")

    def __init__(self, username, password, email, date_of_birth, country, role="USER"):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.email = email
        self.date_of_birth = date_of_birth
        self.country = country
        self.role = role

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def check_user(password, username=None, email=None):
        if username is not None:
            search_user = User.query.filter_by(username=username).first()
            if search_user is None:
                return False
            pass_check = bcrypt.check_password_hash(search_user.password, password)
            if pass_check is True:
                return search_user
            else:
                return False
        elif email is not None:
            search_user = User.query.filter_by(email=email).first()
            if search_user is None:
                return False
            pass_check = bcrypt.check_password_hash(search_user.password, password)
            if pass_check is True:
                return search_user
            else:
                return False

    @staticmethod
    def check_if_username_exists(username):
        search_user = User.query.filter_by(username=username).first()
        if search_user is None:
            return False
        return True

    @staticmethod
    def check_if_email_exists(email):
        search_user = User.query.filter_by(email=email).first()
        if search_user is None:
            return False
        return True
