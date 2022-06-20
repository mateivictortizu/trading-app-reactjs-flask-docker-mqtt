from flask import jsonify

from app.utils.myjwt import MyJWT


def validate_Token(jwt_token, current_app):
    token_decoded = MyJWT.decode_auth_token(jwt_token, jwt_secret=current_app.config['JWT_SECRET_KEY'])
    if token_decoded[0] == -1 or token_decoded[0] == -2:
        return jsonify({'error': 'Token {}'.format(token_decoded[1])}), 403
    else:
        return jsonify({'user': token_decoded[1], 'type_user': token_decoded[2]}), 200
