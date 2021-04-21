from django import forms
from django.forms.models import ModelMultipleChoiceField
from .models import ActionRequest, PlayerAction, Narrative
from users.models import DragonUser


class NewGameForm(forms.Form):
    gameName = forms.CharField(max_length=40)
    gamePlayers = ModelMultipleChoiceField(
        queryset=DragonUser.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class NewGameNote(forms.Form):
    body = forms.CharField(max_length=280)


class NarrativeForm(forms.ModelForm):
    class Meta:
        model = Narrative
        fields = ['text']


class ActionRequestForm(forms.ModelForm):
    class Meta:
        model = ActionRequest
        fields = ['text']


class PlayerActionForm(forms.ModelForm):
    class Meta:
        model = PlayerAction
        fields = [
            'characters',
            'difficulty',
            'related_skill',
        ]
        widgets = {
            'characters': forms.CheckboxSelectMultiple(),
        }
