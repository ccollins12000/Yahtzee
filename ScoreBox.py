import abc
import Die

class ScoreBox:

    def __init__(self):
        self._points = 0
        self._assigned = False

    @property
    def points(self):
        return self._points

    def getpoints(self):
        return self._points

    @property
    def assigned(self):
        return self._assigned

    def getassigned(self):
        return self._assigned

    @abc.abstractmethod
    def assign_points(self, value):
        pass


class Aces(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            points = 0
            for die in dice:
                if die.value == 1:
                    points += 1
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Aces: ' + str(self._points)



dice = Dice.Dice()
for i in range(6):
    dice.add_die(Die.Die())

aces = Aces()

print(aces)
aces.assign_points(dice)
print(aces)

print(dice)