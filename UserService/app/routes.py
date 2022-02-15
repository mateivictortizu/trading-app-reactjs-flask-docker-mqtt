from datetime import datetime
from flask import request
from app import app, db
from app.models import User


@app.route("/register", methods=["POST"])
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    date_of_birth_str = request.json['date_of_birth']
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')
    country = request.json['country']
    user = User(username=username, password=password, email=email, date_of_birth=date_of_birth, country=country)
    db.session.add(user)
    db.session.commit()

    return 'User registration completed', 201
