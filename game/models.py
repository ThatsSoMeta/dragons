from django.db import models
import uuid
from users.models import DragonUser
# from characters.helpers import roll_dice
from characters.models import Character

# Create your models here.


class Game(models.Model):
    gameID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    gameName = models.CharField(max_length=40)
    gameMaster = models.ForeignKey(DragonUser, on_delete=models.CASCADE)
    gamePlayers = models.ManyToManyField(
        DragonUser,
        related_name='players',
        symmetrical=False,
        blank=True
    )
    gameCharacters = models.ManyToManyField(
        Character,
        related_name='pawns',
        symmetrical=True,
        blank=True
    )

    def __str__(self):
        return f"{self.gameName} | {self.gameID}"


class GameNotes(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game} | {self.body} | {self.createdAt}"


class ActionRequest(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(DragonUser, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)


class PlayerAction(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (PENDING, PENDING),
        (ACCEPTED, ACCEPTED),
        (REJECTED, REJECTED)
    ]

    PASS = 'auto pass'
    EASY = 'very easy'
    PRETTY_EASY = 'somewhat easy'
    MODERATE = 'moderate'
    PRETTY_HARD = 'somewhat hard'
    HARD = 'very hard'
    LUDICROUS = 'nearly impossible'

    DIFFICULTY_OPTIONS = [
        (PASS, 0),
        (EASY, 5),
        (PRETTY_EASY, 10),
        (MODERATE, 15),
        (PRETTY_HARD, 20),
        (HARD, 25),
        (LUDICROUS, 30),
    ]

    STR = 'strength'
    DEX = 'dexterity'
    CON = 'constitution'
    INT = 'intelligence'
    WIS = 'wisdom'
    CHA = 'charisma'

    ABILITY_CHOICES = [
        (STR, STR),
        (DEX, DEX),
        (CON, CON),
        (INT, INT),
        (WIS, WIS),
        (CHA, CHA)
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    players = models.ManyToManyField(
        DragonUser,
        symmetrical=False,
        related_name='responsible'
    )
    characters = models.ManyToManyField(
        Character,
        symmetrical=False,
        related_name='characters'
    )
    difficulty = models.CharField(
        max_length=50,
        choices=DIFFICULTY_OPTIONS,
        default=MODERATE
    )
    related_skill = models.CharField(
        max_length=30,
        choices=ABILITY_CHOICES,
        default=None
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    # What the player wants to do
    action_text = models.CharField(max_length=250)
    requested_by = models.ForeignKey(DragonUser, on_delete=models.CASCADE)
    player_character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # The actual result based on roll
    result_text = models.CharField(max_length=250, blank=True, null=True)
    success = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    # def ability_check(self, num_of_dice=1, sides=20):
    #     best_roll = max(roll_dice(num_of_dice, sides))
    #     print(best_roll)


class Narrative(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
