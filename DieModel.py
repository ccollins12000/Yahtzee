import random as r

class Die:
    """
    This is a class for a 6 sided die that can be rolled

    Attributes:
        value (int): the value of the last roll
    """
    def __init__(self, value=None):
        if value is None:
            self._value = 0
            self.roll()
        else:
            if 1 <= value <= 6:
                self._value = value
            else:
                raise Exception('The value of a die must be between 1 and 6')

        self._selected = True

    def roll(self):
        """Rolls the die"""
        self._value = r.randrange(1, 7)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "A die with value of " + str(self.value) + '\n'

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value + other

    def __int__(self):
        return self.value

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    # def __long__(self):
    #     return self.value)

    def __float__(self):
        return float(self.value)

    def __oct__(self):
        return oct(self.value)

    def __hex__(self):
        return hex(self.value)

    def __complex__(self):
        return complex(self.value)

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return self.value

    def __abs__(self):
        return abs(self.value)

    def __invert__(self):
        return ~self.value




