"""This module contains code for a player model

"""
from ScoreCardModel import *

class Player:
    """
    A player object
    """
    def __init__(self, player_name, avatar_file, player_type):
        """The player constructor

        Args:
            player_name (str): The name of the player
            avatar_file (str): The file path to the avatar picture file
            player_type (str): Computer or Human
        """
        self._player_name = player_name
        self._score_card = ScoreCard()
        self._avatar_file = avatar_file
        self._player_type = player_type

    @property
    def player_name(self):
        """srt: Get the name of the player"""
        return self._player_name

    @property
    def score_card(self):
        """srt: Return a reference to the score card"""
        return self._score_card

    @property
    def avatar_file(self):
        """str: Get the avatar file path"""
        return self._avatar_file

    @property
    def player_type(self):
        """str: Get the player type"""
        return self._player_type
