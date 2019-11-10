def dice_roll_count(dice_list, value_to_count):
    return dice_list.count(value_to_count)


def check_yahtzee(dice_list):
    roll_counts = [dice_list.count(value) for value in range(1, 7)]
    return 5 in roll_counts


def check_full_house(dice_list):
    roll_counts = [dice_list.count(value) for value in range(1, 7)]
    return 2 in roll_counts and 3 in roll_counts


def of_a_kind_size(dice_list):
    return max([dice_list.count(value) for value in range(1,7)])


def straight_size(dice_list):
    # generates list of count dice values 1-6 in order.  Any count of 0 breaks the straight
    roll_counts = [str(dice_list.count(value)) for value in range(1, 7)]
    return len(max(''.join(roll_counts).split('0'), key=len))

# Functions for score boxes


def aces_points(dice_list):
    return dice_list.count(1) * 1


def twos_points(dice_list):
    return dice_list.count(2) * 2


def threes_points(dice_list):
    return dice_list.count(3) * 3


def fours_points(dice_list):
    return dice_list.count(4) * 4


def fives_points(dice_list):
    return dice_list.count(5)* 5


def sixes_points(dice_list):
    return dice_list.count(6) * 6


def three_of_a_kind_points(dice_list):
    if of_a_kind_size(dice_list) >= 3:
        return sum(dice_list)
    else:
        return 0


def four_of_a_kind_points(dice_list):
    if of_a_kind_size(dice_list) >= 4:
        return sum(dice_list)
    else:
        return 0


def full_house_points(dice_list):
    if check_full_house(dice_list) or check_yahtzee(dice_list):
        return 25
    else:
        return 0


def small_straight_points(dice_list):
    if straight_size(dice_list) >= 4 or check_yahtzee(dice_list):
        return 30
    else:
        return 0


def large_straight_points(dice_list):
    if straight_size(dice_list) >= 5 or check_yahtzee(dice_list):
        return 40
    else:
        return 0


def yahtzee_points(dice_list):
    if of_a_kind_size(dice_list) >= 5:
        return 50
    else:
        return 0


def chance_points(dice_list):
    return sum(dice_list)


assign_function_lookup = {
    'Aces': aces_points,
    'Twos': twos_points,
    'Threes': threes_points,
    'Fours': fours_points,
    'Fives': fives_points,
    'Sixes': sixes_points,
    '3 of a Kind': three_of_a_kind_points,
    '4 of a Kind': four_of_a_kind_points,
    'Full House': full_house_points,
    'Small Straight': small_straight_points,
    'Large Straight': large_straight_points,
    'Yahtzee': yahtzee_points,
    'Chance': chance_points
}

score_box_value_lookup = {
    1: 'Aces',
    2: 'Twos',
    3: 'Threes',
    4: 'Fours',
    5: 'Fives',
    6: 'Sixes'
}

class ScoreBox:
    """
    """
    def __init__(self, box_type):
        self._points = 0
        self._assigned = False
        self._name = box_type
        self._calculate_points = assign_function_lookup[box_type]

    @property
    def name(self):
        return self._name

    def getname(self):
        return self._name

    @property
    def points(self):
        return self._points

    @property
    def assigned(self):
        return self._assigned

    def assign_points(self, dice):
        if not self.assigned:
            self._assigned = True
            self._points = self._calculate_points(dice)

    def __str__(self):
        return self._name + ': ' + str(self._points)


class ScoreCard:
    def __init__(self):
        self._yahtzee_count = 0
        self._aces = ScoreBox('Aces')
        self._twos = ScoreBox('Twos')
        self._threes = ScoreBox('Threes')
        self._fours = ScoreBox('Fours')
        self._fives = ScoreBox('Fives')
        self._sixes = ScoreBox('Sixes')
        self._upperSum = 0
        self._upperTotal = 0
        self._bonus = 0
        self._threeOfAKind = ScoreBox('3 of a Kind')
        self._fourOfAKind = ScoreBox('4 of a Kind')
        self._fullHouse = ScoreBox('Full House')
        self._smallStraight = ScoreBox('Small Straight')
        self._largeStraight = ScoreBox('Large Straight')
        self._yahtzee = ScoreBox('Yahtzee')
        self._chance = ScoreBox('Chance')
        self._lowerTotal = 0
        self._grandTotal = 0
        self._upper_section = [self._aces, self._twos, self._threes, self._fours, self._fives, self._sixes]
        self._lower_section = [self._threeOfAKind, self._fourOfAKind, self._fullHouse, self._smallStraight, self._largeStraight, self._yahtzee, self._chance]
        self._boxes = [self._aces, self._twos, self._threes, self._fours, self._fives, self._sixes, self._threeOfAKind,
                       self._fourOfAKind, self._fullHouse, self._smallStraight, self._largeStraight, self._yahtzee, self._chance
                       ]

    def print_points(self, box_index):
        return str(self._boxes[box_index])

    def update_points(self):

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

        if self.get_box("Yahtzee").points > 0:
            total = total + (self._yahtzee_count - 1) * 100 # Yahtzee Bonus

        self._lowerTotal = total

        #Total Points
        self._grandTotal = self._upperTotal + self._lowerTotal

    @property
    def total_points(self):
        return self._grandTotal

    @property
    def upper_total_points(self):
        return self._upperTotal

    @property
    def bonus_points(self):
        return self._bonus

    @property
    def lower_total_points(self):
        return self._lowerTotal

    def get_box(self, box_name):
        for box in self._boxes:
            if box.name == box_name:
                return box

    def assign_roll(self, box_name, dice):
        if check_yahtzee(dice):
            self._yahtzee_count = self._yahtzee_count + 1

        if check_yahtzee(dice) and not self.get_box('Yahtzee').assigned:
            self.get_box('Yahtzee').assign_points(dice)
        elif check_yahtzee(dice) and not self.get_box(score_box_value_lookup[dice[0].value]).assigned:
            self.get_box(score_box_value_lookup[dice[0].value]).assign_points(dice)
        else:
            self.get_box(box_name).assign_points(dice)
        self.update_points()

    def get_box_points(self, box_name):
        box = self.get_box(box_name)
        if box is None:
            if box_name == 'Upper Total':
                return self._upperTotal
            elif box_name == 'Bonus':
                return self._bonus
            elif box_name == 'Lower Total':
                return self._lowerTotal
            elif box_name == 'Grand Total':
                return self._grandTotal
        else:
            return box.points

    def get_box_assigned(self, box_name):
        box = self.get_box(box_name)
        if box is None:
            if box_name == 'Upper Total':
                return True
            elif box_name == 'Bonus':
                return True
            elif box_name == 'Lower Total':
                return True
            elif box_name == 'Grand Total':
                return True
        else:
            return box.assigned

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

