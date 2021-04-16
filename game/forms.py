from django import forms
from django.forms import fields
from django.forms.models import ModelMultipleChoiceField
from .models import Game
from users.models import DragonUser

class NewGameForm(forms.Form):
        
    gameName = forms.CharField(max_length=40)
    gamePlayers = ModelMultipleChoiceField(queryset = DragonUser.objects.all(), widget=forms.CheckboxSelectMultiple)

class NewGameNote(forms.Form):
    body = forms.CharField(max_length=280)