from sqlalchemy.orm import sessionmaker

from app import engine
from app.database.models import Fund


def addFundsDAO(user, value):
    Session = sessionmaker(bind=engine)
    session = Session()
    Fund.add_money(user, value)
    session.commit()
    session.close()


def withdrawFundsDAO(user, value):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = Fund.withdraw_money(user, value)
    session.commit()
    session.close()
    return result


def addFundsAfterSellDAO(user, value):
    Session = sessionmaker(bind=engine)
    session = Session()
    Fund.add_money_after_sell(user, value)
    session.commit()
    session.close()


def withdrawFundsAfterBuyDAO(user, value):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = Fund.withdraw_money_after_buy(user, value)
    session.commit()
    session.close()
    return result


def get_fundsDAO(user):
    Session = sessionmaker(bind=engine)
    session = Session()
    value = Fund.get_value_of_user(user)
    session.commit()
    session.close()
    return value
