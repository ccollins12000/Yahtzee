"""Model for Yahtzee game

This module contains the logic code for a yahtzee game

"""

from DieModel import *
from ScoreCardModel import *


class YahtzeeModel:
    """All the logic code for running a yahtzee game

    """
    def __init__(self):
        """
        The constructor for a yahtzee game

        Notes:
            After the game is constructed.  Use the add_player method to add players and the start_game method to begin the game.
        """
        self._players = []
        self._game_started = False
        self._game_complete = False
        self._current_player = -1
        self._turn = 0 # begin game calls next turn which at current player = 0 subtracts this down to 13
        self._rolls_remaining = 0
        self._dice = []
        self._winner = None
        self._assigned_roll = False
        self._instructions = ''
        for die_index in range(5):
            # self._dice.append(Die())
            self._dice.append(Die())

    @property
    def instructions(self):
        """str: The instructions for the player on what to do next"""
        return self._instructions

    @instructions.setter
    def instructions(self, value):
        self._instructions = value

    @property
    def game_over(self):
        """bool: whether or not the game is over"""
        return self._game_complete

    @property
    def current_player(self):
        """obj: the current player object"""
        player_index = self._turn % len(self._players)
        if len(self._players) > 0 and self._turn > 0:
            return self._players[player_index]
        else:
            return None

    @property
    def rolls_remaining(self):
        """int: Get the number of rolls remaining for the current turn"""
        return self._rolls_remaining

    @property
    def turn(self):
        """int: Return the number of turns remaining in the game"""
        return self._turn

    def start_game(self):
        """Starts the game

        Notes:
            The must be players to start the game.  the add_players method can be used to add players

        Raises:
            Exception: If there are no players in the game yet

        """
        self._game_complete = False
        if len(self._players) > 0:
            self._turn = len(self._players) * 13
            self.setup_turn()
            self._game_started = True
        else:
            raise Exception('There must be at least one player to start the game.')

    def add_player(self, player):
        """Add a player to the game

        Args:
            player (obj): The player object to add to the game
        """
        self._players.append(player)

    def remove_player(self, player_index):
        """Removes the player at the given index from the game

        Args:
            player_index (int): The index of the player to remove

        Returns:
            The player object removed from the game
        """
        return self._players.pop(player_index)

    def get_dice(self):
        """Gets the current values of the dice

        Returns:
            A list containing all of the values of the dice
        """
        return [die.value for die in self._dice]

    def roll_dice(self):
        """Rolls all the dice that have been selected

        Returns:
            A list containing all of the values of the dice
        """
        if self._rolls_remaining > 0 and not self._assigned_roll:
            for die_index, die in enumerate(self._dice):
                if die.selected:
                    die.roll()
            self._rolls_remaining = self._rolls_remaining - 1
        return self.get_dice()

    def assign_roll(self, box_name):
        """Assigns the current roll to the score box given

        Note:
            Assigning to a box that already had a roll assigned will do nothing

        Args:
            box_name (str): The name of the box to assign the roll to. Possible values are the following:
            'Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance'

        Returns:
            The resulting points or if the box already is assigned the current points in the box
        """
        score_card = self.current_player.score_card
        # only assign roll if the box doesn't already have value and the roll hasn't already been assigned this turn
        if self._assigned_roll or score_card.get_box_assigned(box_name) or not self._game_started:
            return score_card.get_box_points(box_name)
        else:
            score_card.assign_roll(box_name, self._dice)
            self._assigned_roll = True
            return score_card.get_box_points(box_name)

    def setup_turn(self):
        """A helper function for setting up a turn

        """
        # Setup and roll dice
        self._rolls_remaining = 3
        self._assigned_roll = False
        for die in self._dice:
            die.selected = True
        self.roll_dice()

    def next_turn(self):
        """Moves the game to the next turn.  If it is the last turn, ends the game.

        """
        if self._game_started and not self._game_complete and self._assigned_roll == True:
            self._turn = self._turn - 1
            if self._turn > 0:
                self.setup_turn()
            else:
                self.end_game()

    def end_game(self):
        """Ends the game and calculates winner"""
        self._game_started = False
        self._game_complete = True


