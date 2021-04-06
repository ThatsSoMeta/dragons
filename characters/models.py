from django.db import models

# Create your models here.


class CustomCharacter(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey('DragonUser')
    concept = models.CharField(max_length=280)
    level = models.IntegerField(default=1)
