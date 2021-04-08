from django.db import models
# from django import forms
from users.models import DragonUser

# Create your models here.
# Trying to find a more DRY way to do the stats

CLASS_OPTIONS = [
    ('barbarian', 'Barbarian'),
    ('bard', 'Bard'),
    ('cleric', 'Cleric'),
    ('druid', 'Druid'),
    ('fighter', 'Fighter'),
    ('monk', 'Monk'),
    ('paladin', 'Paladin'),
    ('ranger', 'Ranger'),
    ('rogue', 'Rogue'),
    ('sorcerer', 'Sorcerer'),
    ('warlock', 'Warlock'),
    ('wizard', 'Wizard'),
    ('artificer', 'Artificer'),
]

ALIGNMENT_OPTIONS = [
    ('LG', 'lawful-good'),
    ('NG', 'neutral-good'),
    ('CG', 'chaotic-good'),
    ('LN', 'lawful-neutral'),
    ('NN', 'neutral-neutral'),
    ('CN', 'chaotic-neutral'),
    ('LE', 'lawful-evil'),
    ('NE', 'neutral-evil'),
    ('CE', 'chaotic-evil'),
]


class CharacterSheet(models.Model):
    name = models.CharField(max_length=50)
    player = models.ForeignKey(DragonUser, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    class_name = models.CharField(
        max_length=25,
        choices=CLASS_OPTIONS,
        default=None,
    )
    race = models.CharField(max_length=20)
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
