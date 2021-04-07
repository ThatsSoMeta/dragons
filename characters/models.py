from django.db import models

# Create your models here.
# Trying to find a more DRY way to do the stats


class CharacterSheet(models.Model):
    name = models.CharField(max_length=50)
#    player = models.ForeignKey('DragonUser', on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    race = models.CharField(max_length=20)
    alignment = models.CharField(max_length=25)
    background = models.CharField(max_length=25)
    proficiency_bonus = models.IntegerField()
    armorclass = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    temp_hp = models.IntegerField()
    feats_traits = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)


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
