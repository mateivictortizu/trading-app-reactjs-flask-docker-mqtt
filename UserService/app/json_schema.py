register_schema = {
    'required': ['username', 'password', 'email', 'date_of_birth', 'country'],
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'},
        'email': {'type': 'string'},
        'date_of_birth': {'type': 'string'},
        'country': {'type': 'string'}
    }
}

login_schema = {
    'required': ['identifier', 'password'],
    'properties': {
        'identifier': {'type': 'string'},
        'password': {'type': 'string'}
    }
}
