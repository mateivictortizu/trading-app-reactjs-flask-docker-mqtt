import random
from datetime import datetime, timedelta

from sqlalchemy import desc

from app import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    nationality = db.Column(db.String(3), nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    date_of_registration = db.Column(db.DateTime, nullable=False)
    country = db.Column(db.String(3), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="USER")
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    twoFA = db.Column(db.Boolean, nullable=False, default=True)
    validated_by_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, password, email, name, surname, address, nationality, phone, date_of_birth, country,
                 role="USER"):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.email = email
        self.name = name
        self.surname = surname
        self.address = address
        self.nationality = nationality
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.date_of_registration = datetime.utcnow()
        self.country = country
        self.role = role

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def check_user(password, identifier=None):
        if identifier is not None:
            search_user = User.query.filter_by(username=identifier).first()
            search_email = User.query.filter_by(email=identifier).first()
            if search_user is None:
                pass
            else:
                pass_check = bcrypt.check_password_hash(search_user.password, password)
                if pass_check is True:
                    return True
                else:
                    return False

            if search_email is None:
                pass
            else:
                pass_check = bcrypt.check_password_hash(search_email.password, password)
                if pass_check is True:
                    return True
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

    @staticmethod
    def get_user_by_identifier(identifier):
        search_user = User.query.filter_by(email=identifier).first()
        if search_user is not None:
            return search_user
        search_user = User.query.filter_by(username=identifier).first()
        if search_user is not None:
            return search_user
        return None

    @staticmethod
    def change_pass(identifier, password, new_password):
        check_user = User.check_user(password=password, identifier=identifier)
        if check_user is False:
            return False
        search_user = User.get_user_by_identifier(identifier)
        search_user.password = bcrypt.generate_password_hash(new_password)
        db.session.commit()
        return True

    @staticmethod
    def verify_user(identifier):
        search_user = User.get_user_by_identifier(identifier)
        search_user.validated_by_admin = True
        db.session.commit()

    @staticmethod
    def add_to_user(user):
        db.session.add(user)
        db.session.commit()


class Token(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_token(auth_token):
        res = Token.query.filter_by(token=str(auth_token)).first()
        if res:
            if res.blacklisted:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    def add_to_token(token):
        db.session.add(token)
        db.session.commit()

    @staticmethod
    def blacklisted_token(auth_token):
        res = Token.query.filter_by(token=str(auth_token)).first()
        if res:
            res.blacklisted = True
            db.session.commit()
            return True
        else:
            return False


class OTP(db.Model):
    __tablename__ = 'otps'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issue_date = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    number_of_tries = db.Column(db.Integer, default=0)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.issue_date = datetime.utcnow()
        self.code = random.choice(range(1000, 9999))

    @staticmethod
    def check_otp(identifier, code):
        date_now = datetime.utcnow() + timedelta(minutes=-10)
        search_otp = OTP.query.filter_by(username=identifier, code=code).order_by(desc(OTP.issue_date)).first()
        if search_otp:
            if search_otp.issue_date > date_now:
                return True
            else:
                db.session.delete(search_otp)
                db.session.commit()
                return False
        search_otp = OTP.query.filter_by(username=identifier, code=code).order_by(desc(OTP.issue_date)).first()
        if search_otp:
            if search_otp.issue_date > date_now:
                return True
            else:
                db.session.delete(search_otp)
                db.session.commit()
                return False
        return False

    @staticmethod
    def add_to_otp(otp):
        db.session.add(otp)
        db.session.commit()

    @staticmethod
    def delete_all_otp_from_identifier(identifier):
        OTP.query.filter_by(username=identifier).delete()
        db.session.commit()

    @staticmethod
    def increment_no_of_tries(identifier):
        date_now = datetime.utcnow() + timedelta(minutes=-10)
        search_otp = OTP.query.filter_by(username=identifier).order_by(desc(OTP.issue_date)).first()
        if search_otp:
            if search_otp.issue_date > date_now:
                search_otp.number_of_tries = search_otp.number_of_tries + 1
                if search_otp.number_of_tries > 3:
                    db.session.delete(search_otp)
                db.session.commit()
                return True
            else:
                db.session.delete(search_otp)
                db.session.commit()
                return False
        return False


class OTPToken(db.Model):
    __tablename__ = 'OTPtokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_token(auth_token):
        res = OTPToken.query.filter_by(token=str(auth_token)).first()
        if res:
            if res.blacklisted:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    def add_to_token(token):
        db.session.add(token)
        db.session.commit()

    @staticmethod
    def blacklist_otp_token(token):
        res = OTPToken.query.filter_by(token=str(token)).first()
        res.blacklisted = True
        db.session.commit()
