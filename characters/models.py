from django.db import models
# from django import forms
from users.models import DragonUser

# Create your models here.
# Trying to find a more DRY way to do the stats


class CharacterSheet(models.Model):

    # CLASSES
    BARBARIAN = 'barbarian'
    BARD = 'bard'
    CLERIC = 'cleric'
    DRUID = 'druid'
    FIGHTER = 'fighter'
    MONK = 'monk'
    PALADIN = 'paladin'
    RANGER = 'ranger'
    ROGUE = 'rogue'
    SORCERER = 'sorcerer'
    WARLOCK = 'warlock'
    WIZARD = 'wizard'
    ARTIFICER = 'artificer'

    CLASS_OPTIONS = [
        (BARBARIAN, BARBARIAN),
        (BARD, BARD),
        (CLERIC, CLERIC),
        (DRUID, DRUID),
        (FIGHTER, FIGHTER),
        (MONK, MONK),
        (PALADIN, PALADIN),
        (RANGER, RANGER),
        (ROGUE, ROGUE),
        (SORCERER, SORCERER),
        (WARLOCK, WARLOCK),
        (WIZARD, WIZARD),
        (ARTIFICER, ARTIFICER),
    ]

    # RACES
    DRAGON = 'dragonborn'
    DWARF = 'dwarf'
    ELF = 'elf'
    GNOME = 'gnome'
    HALFELF = 'half-elf'
    HALFORC = 'half-orc'
    HALFLING = 'halfling'
    HUMAN = 'human'
    TIEFLING = 'tiefling'

    RACE_OPTIONS = [
        (DRAGON, DRAGON),
        (DWARF, DWARF),
        (ELF, ELF),
        (GNOME, GNOME),
        (HALFELF, HALFELF),
        (HALFORC, HALFORC),
        (HALFLING, HALFLING),
        (HUMAN, HUMAN),
        (TIEFLING, TIEFLING)
    ]

    # ALIGNMENTS
    LG = 'lawful-good'
    NG = 'neutral-good'
    CG = 'chaotic-good'
    LN = 'lawful-neutral'
    NN = 'neutral'
    CN = 'chaotic-neutral'
    LE = 'lawful-evil'
    NE = 'neutral-evil'
    CE = 'chaotic-evil'

    ALIGNMENT_OPTIONS = [
        (LG, LG),
        (NG, NG),
        (CG, CG),
        (LN, LN),
        (NN, NN),
        (CN, CN),
        (LE, LE),
        (NE, NE),
        (CE, CE)
    ]

    name = models.CharField(max_length=50)
    player = models.ForeignKey(DragonUser, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    class_name = models.CharField(
        max_length=25,
        choices=CLASS_OPTIONS,
        default=None,
    )
    race = models.CharField(
        max_length=20,
        choices=RACE_OPTIONS,
        default=None,
    )
    alignment = models.CharField(
        max_length=25,
        choices=ALIGNMENT_OPTIONS,
        default=None,
    )
    background = models.CharField(max_length=25, blank=True, null=True)
    proficiency_bonus = models.IntegerField(default=0)
    armorclass = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    temp_hp = models.IntegerField(default=0)
    feats_traits = models.CharField(max_length=255, blank=True, null=True)
    equipment = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)


class SpellSheet(models.Model):
    spell_name = models.CharField(max_length=60)
    spell_type = models.CharField(max_length=40)
    casting_time = models.CharField(max_length=25)
    spell_range = models.IntegerField()
    spell_components = models.CharField(max_length=200)
    spell_duration = models.IntegerField()
    spell_description = models.CharField(max_length=200)


class CharacterDescriptions(models.Model):
    personality = models.CharField(max_length=255)
    apperance = models.CharField(max_length=255)
    backstory = models.CharField(max_length=255)
