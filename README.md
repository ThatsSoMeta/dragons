

Character concept? general pre-filled concepts to customize

Race:(check race options for selector)
    -Subrace

Class:
    -barbarian
    -bard
    -cleric
    -druid
    -fighter
    -monk
    -paladin
    -ranger
    -rogue
    -sorcerer
    -warlock
    -wizard
    -articifer(?)

Ability Scores:
    -Strength
    -Dexterity
    -Constitution
    -Intelligence
    -Wisdom
    -Charisma

Description & Background:

Ability score modifiers


Character creation model concept:
{
    'name': charfield
    'class': fk_class
    'level': intfield
    'background': fk_background
    'player_name': fk_user_username
    'faction': fk_factions(?)
    ...more to come
}

