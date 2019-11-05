import YahtzeeModel
dice = [YahtzeeModel.Die() for i in range(5)]
print(dice)
for die in dice:
    print(die.value, end = '')
    print()


points = {}


max_value = -1
max_score_box = ''
for score_box in YahtzeeModel.assign_function_lookup.keys():
    current_value = YahtzeeModel.assign_function_lookup[score_box](dice)
    current_box = score_box
    if current_value > max_value:
        max_value = current_value
        max_score_box = current_box

print(max_score_box, max_value)



