from django.db import models

# Create your models here.
# Trying to find a more DRY way to do the stats

class CharacterSheet(models.Model):
    name = models.CharField(max_length=50)
    player = models.ForeignKey('DragonUser')
    level = models.IntegerField(default=1)
    race = models.CharField(max_length=20)
    alignment = models.CharField(max_length=25)
    background = models.CharField(max_length=25)

class SpellSheet(models.Model):
    spell_name = models.CharField(max_length=60)
    spell_type = models.CharField(max_length=40)
    casting_time = models.CharField(max_length=25)
    spell_range = models.IntegerField()
    spell_components = models.CharField(max_length=200)
    spell_duration = models.IntegerField()
    spell_description = models.CharField(max_length=200)

class CharacterDescriptions(models.Model):
    ...