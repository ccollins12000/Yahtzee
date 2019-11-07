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
counts = {value:dice.count(value) for value in dice}
print(counts)


# Dice with highest match
roll_count = 3
if roll_count > 0:
    print(max(dice, key=dice.count))

print(Y.straight_size(dice))


# def full_house_odds(dice, remaining_rolls):
#     counts = {value: dice.count(value) for value in dice}
#     possible_rolls = 6*5
#     roll_combinations = len(list(i.combinations([1,2,3,4,5], 3)))
#     total_possibilities = possible_rolls * roll_combinations






