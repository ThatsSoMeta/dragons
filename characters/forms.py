from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'class_name', 'alignment']
        widgets = {
            'alignment': forms.RadioSelect(),
            'class_name': forms.RadioSelect(),
            'race': forms.RadioSelect(),
        }
