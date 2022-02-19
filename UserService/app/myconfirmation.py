from itsdangerous import URLSafeTimedSerializer


class MyConfirmation:
    @staticmethod
    def generate_confirmation_token(email, secret, security_pass):
        serializer = URLSafeTimedSerializer(secret)
        return serializer.dumps(email, salt=security_pass)

    @staticmethod
    def confirm_token(token, secret, security_pass, expiration=3600):
        serializer = URLSafeTimedSerializer(secret)
        try:
            email = serializer.loads(
                token,
                salt=security_pass,
                max_age=expiration
            )
        except:
            return False
        return email
