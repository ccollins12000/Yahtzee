import abc
import Die


class ScoreBox:

    def __init__(self):
        self._points = 0
        self._assigned = False
        self._name = ''

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

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
    def __init__(self):
        super().__init__()
        self._name = 'Aces'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(1)
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Aces: ' + str(self._points)


class Twos(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Twos'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(2)*2
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Twos: ' + str(self._points)


class Threes(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Threes'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(3)*3
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Threes: ' + str(self._points)


class Fours(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Fours'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(4)*4
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Fours: ' + str(self._points)


class Fives(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Fives'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(5)*5
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Fives: ' + str(self._points)


class Sixes(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Sixes'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(6)*6
            self._points = points
            self._assigned = True

    def __str__(self):
        return 'Sixes: ' + str(self._points)


class ThreeOfAKind(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Three of a Kind'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            if Die.of_a_kind_size(dice) >= 3:
                self._points = sum(dice)
            else:
                self._points = 0

    def __str__(self):
        return '3 of a Kind: ' + str(self._points)


class FourOfAKind(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Four of a Kind'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            if Die.of_a_kind_size(dice) >= 4:
                self._points = sum(dice)
            else:
                self._points = 0

    def __str__(self):
        return '4 of a Kind: ' + str(self._points)


class FullHouse(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Full House'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            if Die.check_full_house(dice):
                self._points = 25
            else:
                self._points = 0

    def __str__(self):
        return 'Full House: ' + str(self._points)


class SmallStraight(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Small Straight'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            if Die.straight_size(dice) >= 4:
                self._points = 30
            else:
                self._points = 0

    def __str__(self):
        return 'Small Straight: ' + str(self._points)


class LargeStraight(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Large Straight'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            if Die.straight_size(dice) >= 5:
                self._points = 40
            else:
                self._points = 0

    def __str__(self):
        return 'Large Straight: ' + str(self._points)


class Chance(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Chance'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            self._points = sum(dice)

    def __str__(self):
        return 'Chance: ' + str(self._points)


class Yahtzee(ScoreBox):
    def __init__(self):
        super().__init__()
        self._name = 'Yahtzee'

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    def assign_points(self, dice):
        if not self.assigned:
            if Die.of_a_kind_size(dice) == 5:
                self._points = 50
            else:
                self._points = 0

    def __str__(self):
        return 'Yahtzee: ' + str(self._points)


class ScoreCard:
    def __init__(self):
        self._aces = Aces()
        self._twos = Twos()
        self._threes = Threes()
        self._fours = Fours()
        self._fives = Fives()
        self._sixes = Sixes()
        self._upperSum = 0
        self._upperTotal = 0
        self._bonus = 0
        self._threeOfAKind = ThreeOfAKind()
        self._fourOfAKind = FourOfAKind()
        self._fullHouse = FullHouse()
        self._smallStraight = SmallStraight()
        self._largeStraight = LargeStraight()
        self._yahtzee = Yahtzee()
        self._chance = Chance()
        self._lowerTotal = 0
        self._grandTotal = 0
        self._upper_section = [self._aces, self._twos, self._threes, self._fours, self._fives, self._sixes]
        self._lower_section = [self._threeOfAKind, self._fourOfAKind, self._fullHouse, self._smallStraight, self._largeStraight, self._yahtzee, self._chance]
        self._boxes = [self._aces, self._twos, self._threes, self._fours, self._fives, self._sixes, self._threeOfAKind, self._fourOfAKind, self._fullHouse, self._smallStraight, self._largeStraight, self._yahtzee, self._chance]

    def calculate_points(self):

        #Calculate Upper Section
        total = 0
        for box in self._upper_section:
            total += box.points
        self._upperSum = total

        if total >= 63:
            self._bonus = 35
            total += 35
        self._upperTotal = total

        # Calculate Lower Section
        total = 0
        for box in self._lower_section:
            total += box.points

        self._lowerTotal = total

        #Total Points
        self._grandTotal = self._upperTotal + self._lowerTotal

    def assign_roll(self, box_name, dice):
        for box in self._boxes:
            if box.name == box_name:
                box.assign_points(dice)
                break
        self.calculate_points()

    def __lt__(self, other):
        return self._grandTotal < other

    def __le__(self, other):
        return self._grandTotal <= other

    def __eq__(self, other):
        return self._grandTotal == other

    def __ne__(self, other):
        return self._grandTotal != other

    def __ge__(self, other):
        return self._grandTotal >= other

    def __gt__(self, other):
        return self._grandTotal > other

