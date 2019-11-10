from ScoreCardModel import *
from YahtzeeModel import *

dice = [3,3,6,4,1]
dice = [5, 1, 4, 3, 3]
dice = [6,6,6,6,6]

def get_straight(dice):
    counts = [dice.count(value) > 0 for value in range(1, 7)]
    straight_size = []
    occ = 0
    for index in range(len(counts)):
        if counts[index] > 0:
            occ = occ + 1
        else:
            occ = 0
        straight_size.append(occ)

    largest_straight = max(straight_size)
    index = straight_size.index(largest_straight)

    straight = []
    while index > 0:
        if straight_size[index] == 0:
            break
        straight.append(index + 1)
        index = index - 1

    return straight

def dice_in_straight(dice):
    dice_to_keep = []
    occurrence = [dice[0:die_index + 1].count(die) for die_index, die in enumerate(dice)]
    for die_index, die in enumerate(dice):
        if occurrence[die_index] > 1:
            dice_to_keep.append(False)
        elif die == 3 or die == 4:
            dice_to_keep.append(True)
        elif straight_size(dice) < 4 and (die == 6 or die == 1):
            dice_to_keep.append(False)
        else:
            if die in get_straight(dice):
                dice_to_keep.append(True)
            else:
                dice_to_keep.append(False)
    return dice_to_keep

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


def small_straight(dice):
    if straight_size(dice) < 4:
        return dice_in_straight(dice)
    else:
        return [True for index in range(5)]


def large_straight(dice):
    if straight_size(dice) < 5:
        return dice_in_straight(dice)
    else:
        return [True for index in range(5)]



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
    'Sixes': sixes,


}

check_dice_lower = {
    'Small Straight': small_straight,
    'Large Straight': large_straight,
    'Full House': full_house,
    '3 of a Kind': three_of_a_kind,
    '4 of a Kind': four_of_a_kind,
}

check_dice_extras = {
    'Yahtzee': yahtzee,
    'Chance': chance
}

def decide_roll(dice, score_card):
    upper_checks = []
    upper_dice_counts = []
    for box in check_dice_upper:
        if not score_card.get_box_assigned(box):
            upper_checks.append(check_dice_upper[box](dice))
            upper_dice_counts = [sum(dice) for dice in upper_checks]

    lower_checks = []
    lower_dice_counts = []
    for box in check_dice_lower:
        if not score_card.get_box_assigned(box):
            lower_checks.append(check_dice_lower[box](dice))
            lower_dice_counts = [sum(dice) for dice in lower_checks]

    extra_checks = []
    extra_dice_counts = []
    for box in check_dice_extras:
        if not score_card.get_box_assigned(box):
            extra_checks.append(check_dice_extras[box](dice))
            extra_dice_counts = [sum(dice) for dice in extra_checks]

    extra_flag = False
    if len(extra_dice_counts) > 0:
        extra_flag = (min(extra_dice_counts) == 0)
    lower_flag = False
    if len(lower_dice_counts) > 0:
        lower_flag = (min(lower_dice_counts) == 0 )

    #can error here on min if empty
    if extra_flag or (len(upper_checks) == 0 and len(lower_checks) == 0):
        checks = extra_checks
    elif lower_flag or len(upper_checks) == 0:
        checks = lower_checks
    else:
        checks = upper_checks

    return max(checks, key=sum)

def get_highest_score_box(dice, score_card):
    max_value = -1
    max_score_box = ''

    for score_box in assign_function_lookup.keys():
        current_value = assign_function_lookup[score_box](dice)
        current_box = score_box
        if current_value > max_value and not score_card.get_box_assigned(score_box):
            max_value = current_value
            max_score_box = current_box

    return max_score_box

def decide_box(dice, score_card):
    max_value = -1
    max_score_box = ''

    scores = {}

    if of_a_kind_size(dice) != 5 or score_card.get_box_assigned('Yahtzee'):
        for score_box in assign_function_lookup.keys():
            if not score_card.get_box_assigned(score_box):
                scores[score_box] = assign_function_lookup[score_box](dice)
    else:
        return "Yahtzee"

    if scores.get('Full House', 0) == 25:
        return 'Full House'
    elif scores.get('Small Straight', 0) == 30:
        return 'Small Straight'
    elif scores.get('Large Straight', 0) == 40:
        return 'Large Straight'
    elif scores.get('Aces', 0) > 2:
        return "Aces"
    elif scores.get('Twos', 0) > 4:
        return "Twos"
    elif scores.get('Threes', 0) > 8:
        return "Threes"
    elif scores.get('Fours', 0) > 11:
        return "Fours"
    elif scores.get('Fives', 0) > 14:
        return "Fives"
    elif scores.get("Sixes", 0) > 17:
        return "Sixes"
    else:
        return get_highest_score_box(dice, score_card)
