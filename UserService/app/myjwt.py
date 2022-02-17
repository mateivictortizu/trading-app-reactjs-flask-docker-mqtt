import datetime

import jwt


def encode_auth_token(user_id, username, email, role, jwt_secret):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'sub': user_id,
            'username': username,
            'email': email,
            'role': role
        }
        return jwt.encode(
            payload,
            jwt_secret,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token, jwt_secret):
    try:
        payload = jwt.decode(auth_token, jwt_secret, algorithms='HS256')
        return payload['sub'], payload['email'], payload['role']
    except jwt.ExpiredSignatureError:
        return -1, 'EXPIRED'
    except jwt.InvalidTokenError:
        return -2, 'INVALID'
