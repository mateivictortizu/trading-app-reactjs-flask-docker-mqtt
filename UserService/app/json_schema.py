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
    'required': ['identifier', 'code'],
    'properties': {
        'identifier': {'type': 'string'},
        'code': {'type': 'integer'}
    }
}

resend_validate_schema = {
    'required': ['identifier'],
    'properties': {
        'identifier': {'type': 'string'}
    }
}

resend_otp_schema = {
    'required': ['identifier'],
    'properties': {
        'identifier': {'type': 'string'}
    }
}
