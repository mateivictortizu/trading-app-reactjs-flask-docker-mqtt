from datetime import datetime

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import sessionmaker

from app import db, engine


class Invest(db.Model):
    __tablename__ = 'invests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(35), nullable=False)
    stock_symbol = db.Column(db.String(8), nullable=False)
    action_type = db.Column(db.String(4), nullable=False)
    cantitate = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_of_buy = db.Column(db.DateTime, nullable=False)
    CheckConstraint('price >=0', name='priceChecking')
    CheckConstraint('cantitate >=0', name='qtyChecking')

    def __init__(self, user, stock_symbol, action_type, cantitate, price):
        self.user = user
        self.stock_symbol = stock_symbol
        self.action_type = action_type
        self.cantitate = cantitate
        self.price = price
        self.date_of_buy = datetime.utcnow()

    def to_json(self):
        return {"user": self.user, "stock_symbol": self.stock_symbol, "action_type": self.action_type,
                "cantitate": self.cantitate, "price": self.price, "date_of_buy": self.date_of_buy}

    @staticmethod
    def buy_invest(user, stock_symbol, cantitate, price):
        Session = sessionmaker(bind=engine)
        session = Session()
        new_invest = Invest(user, stock_symbol, 'BUY', cantitate, price)
        session.add(new_invest)
        session.commit()
        session.close()

    @staticmethod
    def sell_invest(user, stock_symbol, cantitate, price):
        Session = sessionmaker(bind=engine)
        session = Session()
        new_invest = Invest(user, stock_symbol, 'SELL', cantitate, price)
        session.add(new_invest)
        session.commit()
        session.close()

    @staticmethod
    def get_stock_invest_by_user(user, stock_symbol):
        Session = sessionmaker(bind=engine)
        session = Session()
        list_of_invest = session.query(Invest).filter_by(user=user, stock_symbol=stock_symbol)
        session.commit()
        session.close()
        return list_of_invest

    @staticmethod
    def get_invest_by_user(user):
        Session = sessionmaker(bind=engine)
        session = Session()
        list_of_invest = session.query(Invest).filter_by(user=user)
        session.commit()
        session.close()
        return list_of_invest

    @staticmethod
    def get_users_with_invest():
        Session = sessionmaker(bind=engine)
        session = Session()
        list_of_users = session.query(Invest.user.distinct()).all()
        session.commit()
        session.close()
        return list_of_users
