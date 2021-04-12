from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'race',
            'class_name',
            'alignment',
            'background',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma'
        ]
        widgets = {
            'alignment': forms.RadioSelect(),
            'class_name': forms.RadioSelect(),
            'race': forms.RadioSelect(),
            'background': forms.RadioSelect(),
            'strength': forms.RadioSelect(),
            'dexterity': forms.RadioSelect(),
            'constitution': forms.RadioSelect(),
            'intelligence': forms.RadioSelect(),
            'wisdom': forms.RadioSelect(),
            'charisma': forms.RadioSelect()

        }
