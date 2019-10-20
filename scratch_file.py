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
dice.sort()
print(dice)