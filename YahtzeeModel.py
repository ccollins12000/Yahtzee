import random as r
from ScoreCardModel import *

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





class Player:
    def __init__(self, player_name, avatar_file, player_type):
        self._player_name = player_name
        self._score_card = ScoreCard()
        self._avatar_file = avatar_file
        self._player_type = player_type

    @property
    def player_name(self):
        """Get the name of the player"""
        return self._player_name

    @property
    def score_card(self):
        """Return a reference to the score card"""
        return self._score_card

    @property
    def avatar_file(self):
        return self._avatar_file

    @property
    def player_type(self):
        return self._player_type




class YahtzeeModel:
    def __init__(self):
        self._players = []
        self._game_started = False
        self._current_player = -1
        self._turn = 14 # begin game calls next turn which at current player = 0 subtracts this down to 13
        self._rolls_remaining = 0
        self._dice = []
        self._current_score_card = None
        self._assigned_roll = False
        for die_index in range(5):
            self._dice.append(Die())

    @property
    def current_player(self):
        if len(self._players) > 0:
            return self._players[self._current_player]
        else:
            return None

    @property
    def score_card(self):
        return self._current_score_card

    @property
    def rolls_remaining(self):
        """Get the number of rolls remaining for the current turn"""
        return self._rolls_remaining

    @property
    def turn(self):
        """Return the number of turns remaining in the game"""
        return self._turn

    def start_game(self):
        if len(self._players) > 0:
            self.next_turn()
            self._game_started = True
        else:
            raise Exception('There must be at least one player to start the game.')

    def add_player(self, player):
        self._players.append(player)

    def remove_player(self, player_index):
        return self._players.pop(player_index)

    def get_dice(self):
        return [die.value for die in self._dice]

    def roll_dice(self):
        """Roll the dice that have been selected"""
        if self._rolls_remaining > 0 and not self._assigned_roll:
            for die_index, die in enumerate(self._dice):
                if die.selected:
                    die.roll()
            self._rolls_remaining = self._rolls_remaining - 1
        return self.get_dice()

    def assign_roll(self, box_name):
        # only assign roll if the box doesn't already have value and the roll hasn't already been assigned this turn
        if self._assigned_roll or self._current_score_card.get_box_assigned(box_name) or not self._game_started:
            return self._current_score_card.get_box_points(box_name)
        else:
            self._current_score_card.assign_roll(box_name, self._dice)
            self._assigned_roll = True
            return self._current_score_card.get_box_points(box_name)

    def next_turn(self):
        """Proceed to next turn"""
        if self._assigned_roll or not self._game_started:
            if self._turn > 0:
                self._current_player = (self._current_player + 1) % len(self._players)

                self._current_score_card = self._players[self._current_player].score_card
                if self._current_player == 0:
                    self._turn -= 1
                self._rolls_remaining = 3
                for die in self._dice:
                    die.selected = True
                self._assigned_roll = False
                self.roll_dice()
            else:
                self.end_game()

    def end_game(self):
        """End the game and calculate winner"""
        pass

    def toggle_die_for_roll(self, die_index, selected):
        """Select or un-select dice to be rolled"""
        self._selected_dice[die_index] = selected
        # return [self._selected_dice[selected_index] for selected_index in self._selected_dice]


