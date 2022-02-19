register_schema = {
    'required': ['username', 'password', 'email', 'date_of_birth', 'country', 'name', 'surname', 'address',
                 'nationality', 'phone'],
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'},
        'email': {'type': 'string'},
        'date_of_birth': {'type': 'string'},
        'country': {'type': 'string'},
        'name': {'type': 'string'},
        'surname': {'type': 'string'},
        'address': {'type': 'string'},
        'nationality': {'type': 'string'},
        'phone': {'type': 'string'}
    }
}

login_schema = {
    'required': ['identifier', 'password'],
    'properties': {
        'identifier': {'type': 'string'},
        'password': {'type': 'string'}
    }
}

validate_otp_schema = {
    'required': ['code'],
    'properties': {
        'code': {'type': 'integer'}
    }
}

resend_validate_schema = {
    'required': ['identifier'],
    'properties': {
        'identifier': {'type': 'string'}
    }
}

change_password_schema = {
    'required': ['identifier', 'password', 'new_password'],
    'properties': {
        'identifier': {'type': 'string'},
        'password': {'type': 'string'},
        'new_password': {'type': 'string'}
    }
}
