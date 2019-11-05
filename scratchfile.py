import YahtzeeModel
all_rolls_possible = []
for value1 in range(1, 7):
    print(value1)
    for value2 in range(1, 7):
        for value3 in range(1, 7):
            for value4 in range(1, 7):
                for value5 in range(1,7):
                    all_rolls_possible.append([value1, value2, value3, value4, value5])

print(len(all_rolls_possible))

#full house
full_house_rolls = []
total = 0
for roll in all_rolls_possible:
    if YahtzeeModel.check_full_house(roll):
        total += 1
print(total)
full_house_odds = total/len(all_rolls_possible)*100
print('Full house counts: ', total)
print('full house odds: ', full_house_odds)

total = 0
for roll in all_rolls_possible:
    if roll.count(1) == 4:
        total += 1
one_one_odds = total/len(all_rolls_possible)*100
print("four one Count: ", total)
print('four ones: ', one_one_odds)


#small straight
total = 0

for roll in all_rolls_possible:
    if YahtzeeModel.straight_size(roll) >= 4:
        total += 1


small_straight_odds = total/len(all_rolls_possible)*100
print('small straight count: ', total)
print('small straight odds: ', small_straight_odds)

#large straight
total = 0

for roll in all_rolls_possible:
    if YahtzeeModel.straight_size(roll) >= 5:
        total += 1

larges_straight_odds = total/len(all_rolls_possible)*100
print('large straight count: ', total)
print('large straight odds: ', larges_straight_odds)

#Two of a kind
total = 0

for roll in all_rolls_possible:
    if YahtzeeModel.of_a_kind_size(roll) >= 2:
        total += 1

two_of_a_kind_size = total/len(all_rolls_possible)*100
print('two of a kind: ', total)
print('two of a kind odds: ', two_of_a_kind_size)


#sixes odds
counts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

for roll in all_rolls_possible:
    counts[roll.count(6)] += 1/len(all_rolls_possible)*100

print(counts)
# reassin or assign and end turn
# add in text for how scorebox calculated
# option to sort dice
# unselct scorebox when starting new turn
# allow three dice rolls
# choose player order
# unselect all dice at beginning of turn
# select all and unselect all buttons
# calculate odds for each roll
# Keep and roll option columns?
# Error Messages
# multiple yahtzees
# Error Handling if no player is chosen