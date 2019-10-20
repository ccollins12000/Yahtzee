import Die

dice = Die.Dice()
die1 = Die.Die()
die2 = Die.Die()
die3 = Die.Die()
die4 = Die.Die()
die5 = Die.Die()
die6 = Die.Die()

dice.add_die(die1)
dice.add_die(die2)
dice.add_die(die3)
dice.add_die(die4)
dice.add_die(die5)
dice.add_die(die6)

print(dice)



print(dice)
dice.sort()
print(dice)

print('count of dice with 1: ', str(dice.dice_roll_count(1)))
print('count of dice with 2: ', str(dice.dice_roll_count(2)))
print('count of dice with 3: ', str(dice.dice_roll_count(3)))
print('count of dice with 4: ', str(dice.dice_roll_count(4)))
print('count of dice with 5: ', str(dice.dice_roll_count(5)))
print('count of dice with 6: ', str(dice.dice_roll_count(6)))
print('straight length: ', str(Die.straight_size(dice)))
print('of a kind size: ', str(Die.of_a_kind_size(dice)))

print(sum(dice))
