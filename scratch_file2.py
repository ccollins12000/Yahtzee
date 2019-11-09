import YahtzeeModel as Y
# dice = [YahtzeeModel.Die() for i in range(5)]
# print(dice)
# for die in dice:
#     print(die.value, end = '')
#     print()
#
#
# points = {}
#
#
# max_value = -1
# max_score_box = ''
#
# for score_box in YahtzeeModel.assign_function_lookup.keys():
#     current_value = YahtzeeModel.assign_function_lookup[score_box](dice)
#     current_box = score_box
#     if current_value > max_value:
#         max_value = current_value
#         max_score_box = current_box
#
# print(max_score_box, max_value)
#

import itertools as i

# Full_House

dice = [3,3, 5, 6, 2]

def aces(dice):
    return [die == 1 for die in dice]

def twos(dice):
    return [die == 2 for die in dice]

def threes(dice):
    return [die == 3 for die in dice]

def fours(dice):
    return [die == 4 for die in dice]

def fives(dice):
    return [die == 5 for die in dice]

def sixes(dice):
    return [die == 6 for die in dice]

def three_of_a_kind(dice):
    common_die = max(dice,key=dice.count)
    return [die == common_die for die in dice]

def four_of_a_kind(dice):
    common_die = max(dice,key=dice.count)
    return [die == common_die for die in dice]

def small_straight(dice):
    return [False for index in range(5)]

def large_straight(dice):
    return [False for index in range(5)]


def full_house(dice):
    occurence = [dice[0:die_index + 1].count(die) for die_index, die in enumerate(dice)]
    counts = [dice.count(die) for die in dice]
    to_keep = []
    for index in range(len(occurence)):
        to_keep.append( (counts[index] != 1 and occurence[index] in [1,2,3]))
    return to_keep


check_dice = {
    'Aces': aces,
    'Twos': twos,
    'Threes': threes,
    'Fours':  fours,
    'Fives': fives,
    'Sixes': sixes,
    '3 of a Kind': three_of_a_kind,
    '4 of a Kind': four_of_a_kind,
    'Full House': full_house,
    'Small Straight': small_straight,
    'Large Straight': large_straight
}
checks = []
for box in check_dice:
    checks.append( (check_dice[box](dice)) )



print(checks)


#
#
# counts = {value:dice.count(value) for value in dice}
# print(counts)
#
#
# # Dice with highest match
# roll_count = 3
# if roll_count > 0:
#     print(max(dice, key=dice.count))
#
# print(Y.straight_size(dice))
#

# def full_house_odds(dice, remaining_rolls):
#     counts = {value: dice.count(value) for value in dice}
#     possible_rolls = 6*5
#     roll_combinations = len(list(i.combinations([1,2,3,4,5], 3)))
#     total_possibilities = possible_rolls * roll_combinations




class ScoreCardController:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.view_to_model = {
            'Aces': 'Aces', 'Twos': 'Twos', 'Threes': 'Threes', 'Fours': 'Fours', 'Fives': 'Fives', 'Sixes': 'Sixes',
            '3 of a Kind': '3 of a Kind', '4 of a Kind': '4 of a Kind', 'Full House': 'Full House',
            'Small Straight': 'Small Straight', 'Large Straight': 'Large Straight', 'Yahtzee': 'Yahtzee',
            'Chance': 'Chance', 'Bonus': 'Bonus', 'Upper Total': 'Upper Total', 'Lower Total': 'Lower Total',
            'Grand Total': 'Grand Total'
        }

    def update_view(self):
        for box in self._view:
            view_name = box
            model_name = self.view_to_model[box]
            model_points = self._model.get_box_points(model_name)
            model_assigned = self._model.get_box_assigned(model_name)

            if model_assigned:
                self._view.assign_points(view_name, model_points)
            else:
                self._view.assign_points(view_name, '')



