class Player:
    def __init__(self, player_name):
        self._name = player_name

    @property
    def name(self):
        return self._name

    def getname(self):
        return  self._name


class YahtzeeGame:


