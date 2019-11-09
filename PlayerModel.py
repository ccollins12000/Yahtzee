from ScoreCardModel import *

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
