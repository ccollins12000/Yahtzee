from ScoreCardModel import *
from YahtzeeModel import *

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

def yahtzee(dice):
    common_die = max(dice,key=dice.count)
    return [die == common_die for die in dice]

def chance(dice):
    return [die == 6 for die in dice]

def straight(dice):
    if straight_size(dice) < 5:
        dice_to_keep = []
        occurence = [dice[0:die_index + 1].count(die) for die_index, die in enumerate(dice)]
        for die_index, die in enumerate(dice):
            if occurence[die_index] > 1:
                dice_to_keep.append(False)
            elif die == 3 or die == 4:
                dice_to_keep.append(True)
            elif straight_size(dice) < 5 and (die == 1 or die == 6):
                dice_to_keep.append(False)
            else:
                dice_to_keep.append(True)
        return dice_to_keep
    else:
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
    'Small Straight': straight,
    'Large Straight': straight,
    'Yahtzee': yahtzee,
    'Chance': chance
}


def decide_roll(dice, score_card):
    checks = []
    dice_counts = []
    boxes = []
    for box in check_dice_upper:
        if not score_card.get_box_assigned(box):
            boxes.append(box)
            checks.append(check_dice_upper[box](dice))
            dice_counts = [sum(dice) for dice in checks]

    if len(dice_counts) == 0:
        for box in check_dice_lower:
            boxes.append(box)
            checks.append(check_dice_lower[box](dice))
            dice_counts = [sum(dice) for dice in checks]

    rolls = max(checks, key=sum)
    box = boxes[checks.index(rolls)]

    return max(checks, key=sum)


def decide_box(dice, score_card):
    max_value = -1
    max_score_box = ''

    for score_box in assign_function_lookup.keys():
        current_value = assign_function_lookup[score_box](dice)
        current_box = score_box
        if current_value > max_value and not score_card.get_box_assigned(score_box):
            max_value = current_value
            max_score_box = current_box

    return max_score_box
