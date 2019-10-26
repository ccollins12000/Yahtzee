import random as r


class Die:
    def __init__(self):
        self._value = 0
        self.roll()

    def roll(self):
        """Rolls the die"""
        self._value = r.randrange(1, 7)

    def __str__(self):
        return "A die with value of " + str(self.value) + '\n'

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

    def __int__(self):
        return self.value

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


class Dice:
    def __init__(self, number_of_dice=None):
        self._dice = []
        self._current_die_index = 0
        self._last_die_index = -1
        if not number_of_dice is None:
            for die_index in range(number_of_dice):
                self.add_die(Die())

    def add_die(self, die):
        self._dice.append(die)
        self._last_die_index += 1
        self.sort()

    def remove_die(self, index):
        del self._dice[index]
        self._last_die_index += -1
        self.sort()

    def get_die(self, index):
        return self._dice[index]

    def die_count(self):
        return len(self._dice)

    def dice_roll_count(self, value_to_count):
        self.sort()
        return self._dice.count(value_to_count)

    def roll(self):
        for die in self._dice:
            die.roll()
        self.sort()

    def sort(self):
        self._dice.sort()

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
        msg = 'Dice object containing: \n'
        for die in self._dice:
            msg += '\t' + str(die)
        return msg


def check_yahtzee(dice: Dice):
    has_yahtzee = False
    for value in range(1,7):
        if dice.dice_roll_count(value) == 5:
            has_yahtzee = True
    return has_yahtzee


def check_full_house(dice: Dice):
    ones = dice.dice_roll_count(1)
    twos = dice.dice_roll_count(2)
    threes = dice.dice_roll_count(3)
    fours = dice.dice_roll_count(4)
    fives = dice.dice_roll_count(5)
    sixes = dice.dice_roll_count(6)
    if (ones == 2 or twos == 2 or threes == 2 or fours == 2 or fives == 2 or sixes == 2) and \
            (ones == 3 or twos == 3 or threes == 3 or fours == 3 or fives == 3 or sixes == 3):
        return True
    else:
        return False


def of_a_kind_size(dice: Dice):
    counts = [dice.dice_roll_count(1), dice.dice_roll_count(2), dice.dice_roll_count(3), dice.dice_roll_count(4), dice.dice_roll_count(5),
              dice.dice_roll_count(6)]
    return max(counts)


def straight_size(dice: Dice):
    dice.sort()
    straight_length = 1
    longest_straight = 1
    for die_index in range(1, dice.die_count()):
        current_die = dice.get_die(die_index)
        previous_die = dice.get_die(die_index - 1)
        if current_die == previous_die + 1:
            straight_length += 1
            if straight_length > longest_straight:
                longest_straight = straight_length
        elif current_die == previous_die:
            straight_length = straight_length
        else:
            # Restart
            straight_length = 1

    return longest_straight


