import YahtzeeModel
all_rolls_possible = []
for value1 in range(1, 7):
    for value2 in range(1, 7):
        for value3 in range(1, 7):
            for value4 in range(1, 7):
                for value5 in range(1,7):
                    all_rolls_possible.append([value1, value2, value3, value4, value5])

#full house

total = 0
for roll in all_rolls_possible:
    if YahtzeeModel.check_full_house(roll):
        total += 1

full_house_odds = total/len(all_rolls_possible)*100
print('full house odds: ', full_house_odds)

#small straight
total = 0

for roll in all_rolls_possible:
    if YahtzeeModel.straight_size(roll) >= 4:
        total += 1

small_straight_odds = total/len(all_rolls_possible)*100

print('small straight odds: ', small_straight_odds)

#large straight
total = 0

for roll in all_rolls_possible:
    if YahtzeeModel.straight_size(roll) >= 5:
        total += 1

larges_straight_odds = total/len(all_rolls_possible)*100

print('large straight odds: ', larges_straight_odds)

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
