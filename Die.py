import random as r


class die:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = r.randrange(1, 7)

