

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
    'concept': charfield
    'class': fk_class
    'level': intfield, default=1?
    'race': fk_race
    'sub-race': fk_subrace
    'background': fk_background
    'player_name': fk_user_username
    'faction': fk_factions(?)
    'experience_points': intfield, default=1
    'ability_score_options': list of ints, default=[15, 14, 13, 12, 10, 8] # or you can roll for options(possibly)
    'ability_score_categories': many-to-many abilities?
    'abilities': {
        'strength': intfield, default=0
        'dexterity': intfield, default=0
        'constitution': intfield, default=0
        'intelligence': intfield, default=0
        'wisdom': intfield, default=0
        'charisma': intfield, default=0
    }
    'ability-modifiers': {
        'strength': intfield, default=0
        'dexterity': intfield, default=0
        'constitution': intfield, default=0
        'intelligence': intfield, default=0
        'wisdom': intfield, default=0
        'charisma': intfield, default=0
    }
    'features/traits': many-to-many with features/traits?
    'other proficiencies & languages': many-to-many-languages?
    'hit-points': refer to class
    'proficiency-bonus': based on level
    'saving-throws': {
        'strength': intfield, default=0
        'dexterity': intfield, default=0
        'constitution': intfield, default=0
        'intelligence': intfield, default=0
        'wisdom': intfield, default=0
        'charisma': intfield, default=0
    } #refer to class features
    'skills': #choose from given list, refer to class

    ...more to come
}

