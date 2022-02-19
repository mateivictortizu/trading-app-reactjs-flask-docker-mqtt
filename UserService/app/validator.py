import re

country_abbrev = [
    'AC', 'AF', 'AX', 'AL', 'DZ', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD',
    'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH',
    'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY',
    'CZ', 'DK', 'DJ', 'DM', 'DO', 'TP', 'EC', 'EG', 'SV', 'GQ', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF',
    'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN',
    'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR',
    'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT',
    'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'AN',
    'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH',
    'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'UK', 'SN', 'RS', 'SC', 'SL', 'SG',
    'SK', 'SI', 'SB', 'SO', 'AS', 'ZA', 'GS', 'SU', 'ES', 'LK', 'SH', 'KN', 'LC', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SZ',
    'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE',
    'UK', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW'
]


class Validator:
    @staticmethod
    def password_check(password):
        lenght_error = len(password) < 8
        digit_error = re.search(r'\d', password) is None
        uppercase_error = re.search(r'[A-Z]', password) is None
        lowercase_error = re.search(r'[a-z]', password) is None
        symbol_error = re.search(r'\W', password) is None

        check_result = not (lenght_error or digit_error or uppercase_error or lowercase_error or symbol_error)

        return check_result

    @staticmethod
    def email_check(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return True
        else:
            return False

    @staticmethod
    def check_username(username):
        regex = r'^[A-Za-z][A-Za-z0-9_]{7,29}$'
        if re.fullmatch(regex, username):
            return True
        else:
            return False

    @staticmethod
    def check_country(country):
        if country in country_abbrev:
            return True
        else:
            return False

    @staticmethod
    def check_nationality(nationality):
        if nationality in country_abbrev:
            return True
        else:
            return False
