from django.forms import ModelForm
from .models import CharacterSheet, SpellSheet, CharacterDescriptions

class CreateCharacterForm(ModelForm):
    class Meta:
        model = CharacterSheet
        fields = [
            'name',
            'level',
            'race',
            'alignment',
            'background',
            'proficiency_bonus',
            'armorclass',
            'speed',
            'hp',
            'feats_traits',
            'equipment',
            'languages'
        ]


class SpellSheetForm(ModelForm):
    class Meta:
        model = SpellSheet
        fields = [
            'spell_name',
            'spell_type',
            'casting_time',
            'spell_range',
            'spell_components',
            'spell_duration',
            'spell_description'
        ]


class CharacterDescriptionsForm(ModelForm):
    class Meta:
        model = CharacterDescriptions
        fields = [
            'personality',
            'apperance',
            'backstory'
        ]
