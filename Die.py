import random as r


class Die:
    def __init__(self):
        self._value = 0
        self.roll()

    def roll(self):
        """Rolls the die"""
        self._value = r.randrange(1, 7)

    def __str__(self):
        return "A die with value of " + str(self.value)

    @property
    def value(self):
        return self._value

    def getvalue(self):
        return self._value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value + other

    def __int__(self):
        return self.value



class Dice:
    def __init__(self):
        self._dice = []
