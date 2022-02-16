import random


class OTP:

    def __init__(self, destination):
        self.destination = destination
        self.code = random.choice(range(1000, 9999))
