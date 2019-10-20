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
        self._current_die_index = 0
        self._last_die_index = -1

    def add_die(self, die):
        self._dice.append(die)
        self._last_die_index += 1

    def remove_die(self, index):
        del self._dice[index]
        self._last_die_index += -1

    def roll(self):
        for die in self._dice:
            die.roll()

    def __iter__(self):
        self._current_die_index = 0
        return self

    def __next__(self):
        if self._current_die_index > self._last_die_index:
            raise StopIteration
        else:
            self._current_die_index += 1
            return self._dice[self._current_die_index - 1]

    def __str__(self):
        msg = ''
        for die in self._dice:
            msg += str(die)
        return msg


