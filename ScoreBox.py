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
            points = dice.dice_roll_count(1)
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Aces: ' + str(self._points)


class Twos(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(2)*2
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Twos: ' + str(self._points)


class Threes(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(3)*3
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Threes: ' + str(self._points)


class Fours(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(4)*4
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Fours: ' + str(self._points)


class Fives(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(5)*5
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Fives: ' + str(self._points)


class Sixes(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(6)*6
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Sixes: ' + str(self._points)


class ThreeOfAKind(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            if Die.of_a_kind_size(dice) >= 3:
                self._points = sum(dice)
            else:
                self._points = 0

    def __str__(self):
        return '3 of a Kind: ' + str(self._points)


class FourOfAKind(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            if Die.of_a_kind_size(dice) >= 4:
                self._points = sum(dice)
            else:
                self._points = 0

    def __str__(self):
        return '4 of a Kind: ' + str(self._points)


class FullHouse(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            if Die.check_full_house(dice):
                self._points = 25
            else:
                self._points = 0

    def __str__(self):
        return 'Full House: ' + str(self._points)


class SmallStraight(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            if Die.straight_size(dice) >= 4:
                self._points = 30
            else:
                self._points = 0

    def __str__(self):
        return 'Small Straight: ' + str(self._points)


class LargeStraight(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            if Die.straight_size(dice) >= 5:
                self._points = 40
            else:
                self._points = 0

    def __str__(self):
        return 'Large Straight: ' + str(self._points)


class Chance(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            self._points = sum(dice)

    def __str__(self):
        return 'Chance: ' + str(self._points)


class Yahtzee(ScoreBox):
    def assign_points(self, dice):
        if not self.assigned:
            if Die.of_a_kind_size(dice) == 5:
                self._points = 50
            else:
                self._points = 0

    def __str__(self):
        return 'Yahtzee: ' + str(self._points)

