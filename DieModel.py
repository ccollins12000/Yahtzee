"""The Die Object

This module contains all the code for a die object
"""

import random as r

class Die:
    """
    This is a class for a 6 sided die that can be rolled
    """
    def __init__(self, value=None):
        """
        The constructor for a die object

        Args:
            value (int): The initial value of the die. If none is passed it is random.

        Raises:
            Exception: If the value is not between 1 and 6, an error is raised.  This isn't some fancy D&D game, it's just a boring old Yahtzee game!
        """
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
        """bool: Gets or set whether the die is selected"""
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    @property
    def value(self):
        """int: the value of the die"""
        return self._value

    def __str__(self):
        """str: gives a description of the die"""
        return "A die with value of " + str(self.value) + '\n'

    def __add__(self, other):
        """int: adds the die's value"""
        return self.value + other

    def __radd__(self, other):
        """int: adds the die's value"""
        return self.value + other

    def __int__(self):
        """int: returns the die's value"""
        return self.value

    def __lt__(self, other):
        """bool: determines whether the die's value is greater than an integer"""
        return self.value < other

    def __le__(self, other):
        """bool: determines whether the die's value is less than an integer"""
        return self.value <= other

    def __eq__(self, other):
        """bool: determines whether the die's value is equal to an integer"""
        return self.value == other

    def __ne__(self, other):
        """bool: determines whether the die's value is not equal to an integer"""
        return self.value != other

    def __ge__(self, other):
        """bool: determines whether the die's value is greater than or equal to an integer"""
        return self.value >= other

    def __gt__(self, other):
        """bool: determines whether the die's value is greater than an integer"""
        return self.value > other

    # def __long__(self):
    #     return self.value)

    def __float__(self):
        """float: converts the die's value to a float"""
        return float(self.value)

    def __oct__(self):
        """oct: converts the die's value to an oct"""
        return oct(self.value)

    def __hex__(self):
        """hex: converts the die's value to a hex"""
        return hex(self.value)

    def __complex__(self):
        """complex: converts the die's value to a complex"""
        return complex(self.value)

    def __neg__(self):
        """int: returns the opposite of the die's value"""
        return -self.value

    def __pos__(self):
        """int: returns the die's value"""
        return self.value

    def __abs__(self):
        """int: returns the absolute value of the die's value"""
        return abs(self.value)

    def __invert__(self):
        """int: inverts the die's value"""
        return ~self.value




