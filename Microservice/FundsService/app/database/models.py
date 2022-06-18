from sqlalchemy import CheckConstraint

from app import db


class Fund(db.Model):
    __tablename__ = 'funds'

    user = db.Column(db.String(35), primary_key=True)
    value = db.Column(db.Float, default=0)
    all_deposit = db.Column(db.Float, default=0)
    currency = db.Column(db.String(3), default='USD')
    CheckConstraint('value >=0', name='valueChecking')

    def __init__(self, user, value):
        self.user = user
        self.value = value
        self.all_deposit = value

    @staticmethod
    def add_money(user, value):
        search_fund = Fund.query.filter_by(user=user).first()
        if search_fund is None:
            new_fund = Fund(user=user, value=float(value))
            db.session.add(new_fund)
            db.session.commit()
        else:
            search_fund.value = float(search_fund.value) + float(value)
            search_fund.all_deposit = float(search_fund.all_deposit) + float(value)
            db.session.commit()

    @staticmethod
    def withdraw_money(user, value):
        search_fund = Fund.query.filter_by(user=user).first()
        if search_fund is None:
            return False
        else:
            if (float(search_fund.value) - float(value)) >= 0:
                search_fund.value = float(search_fund.value) - float(value)
            db.session.commit()

    @staticmethod
    def add_money_after_sell(user, value):
        search_fund = Fund.query.filter_by(user=user).first()
        if search_fund is None:
            new_fund = Fund(user=user, value=float(value))
            db.session.add(new_fund)
            db.session.commit()
        else:
            search_fund.value = float(search_fund.value) + float(value)
            db.session.commit()

    @staticmethod
    def withdraw_money_after_buy(user, value):
        search_fund = Fund.query.filter_by(user=user).first()
        if search_fund is None:
            return False
        else:
            if (float(search_fund.value) - float(value)) >= 0:
                search_fund.value = float(search_fund.value) - float(value)
            db.session.commit()

    @staticmethod
    def get_value_of_user(user):
        search_fund = Fund.query.filter_by(user=user).first()
        if search_fund is None:
            return False
        else:
            return search_fund.value
