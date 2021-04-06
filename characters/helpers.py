import random


def roll_dice(num_of_dice=1, sides=6):
    rolls = []
    for i in range(num_of_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
    if len(rolls) < 2:
        rolls = rolls[0]
    else:
        rolls.sort()
    return rolls


def roll_for_ability_scores(num_of_abilities=6):
    score_options = []
    while len(score_options) < num_of_abilities:
        rolls = roll_dice(4, 6)
        score_options.append(sum(rolls) - min(rolls))
    score_options.sort()
    return score_options


def determine_modifier(ability_score):
    return ((ability_score - 10) // 2)


my_scores = roll_for_ability_scores()
for score in my_scores:
    print('Score:', score)
    print('Modifier:', determine_modifier(score))
    print()
