from django.contrib import admin
from .models import (
    Game,
    GameNotes,
    ActionRequest,
    PlayerAction,
    Narrative,
    AbilityCheck
)


# Register your models here.
admin.site.register(Game)
admin.site.register(GameNotes)
admin.site.register(ActionRequest)
admin.site.register(PlayerAction)
admin.site.register(Narrative)
admin.site.register(AbilityCheck)
