from ScoreCardModel import *

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
    if straight_size(dice) < 4:
        pass
    else:
        return [True for index in range(5)]

def large_straight(dice):
    return [False for index in range(5)]


def full_house(dice):
    occurence = [dice[0:die_index + 1].count(die) for die_index, die in enumerate(dice)]
    counts = [dice.count(die) for die in dice]
    to_keep = []
    for index in range(len(occurence)):
        to_keep.append( (counts[index] != 1 and occurence[index] in [1,2,3]))
    return to_keep

check_dice_upper = {
    'Aces': aces,
    'Twos': twos,
    'Threes': threes,
    'Fours':  fours,
    'Fives': fives,
    'Sixes': sixes
}

check_dice_lower = {
    '3 of a Kind': three_of_a_kind,
    '4 of a Kind': four_of_a_kind,
    'Full House': full_house,
    'Small Straight': small_straight,
    'Large Straight': large_straight
}


def decide_roll(dice, score_card):
    checks = []
    dice_counts = []
    for box in check_dice_upper:
        if not score_card.get_box_assigned(box):
            checks.append(check_dice_upper[box](dice))
            dice_counts = [sum(dice) for dice in checks]

    return max(checks, key=sum)
