from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DragonUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = DragonUser
        fields = [
            'email',
            'username',
        ]


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    photo_url = forms.URLField(required=False)
