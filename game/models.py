from django.db import models
import uuid
from users.models import DragonUser

# Create your models here.
class Game(models.Model):
    gameID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gameName = models.CharField(max_length=40)
    gameMaster = models.ForeignKey(DragonUser, on_delete=models.CASCADE)
    gamePlayers = models.ManyToManyField(DragonUser,related_name='players', symmetrical=False, blank=True)

    def __str__(self):
        return f"{self.gameName} | {self.gameID}"

class GameNotes(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game} | {self.body} | {self.createdAt}"