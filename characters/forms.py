from django import forms
from .models import CharacterSheet


class CharacterForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = "__all__"
        widgets = {
            'alignment': forms.RadioSelect(),
            'class_name': forms.RadioSelect(),
            'race': forms.RadioSelect(),
        }
