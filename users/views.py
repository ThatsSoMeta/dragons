from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    CreateUserForm,
    LoginForm,
    EditProfileForm,
    CharacterTestForm
)
from .models import DragonUser
from django.views import View
import requests

# Create your views here.


class RegisterView(View):
    form = CreateUserForm()
    template_name = 'auth/register.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                'form': self.form,
                'header': 'Create Account'
            }
        )

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = DragonUser.objects.create_user(
                email=data['email'],
                username=data['username'],
                password=data['password1'],
            )
            login(request, user)
            return redirect(reverse('homepage'))
        print(form.errors)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'header': 'Create Account',
                'errors': form.errors
            }
        )


class LoginView(View):
    form = LoginForm()
    template_name = 'auth/generic_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                'form': self.form,
                'header': 'Login'
            }
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                email=data['email'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get(
                        'next',
                        reverse('homepage')
                    )
                )
            print("Login failed")
            print(authenticate(email=data['email'], password=data['password']))
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'header': 'Login',
                'errors': ['Email and password do not match']
            }
        )


class ProfileView(View):
    form = EditProfileForm()
    template_name = 'auth/edit_profile.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )

    def post(self, request):
        form = EditProfileForm(request.POST)
        user = request.user
        print('User:', user)
        print(form.data)
        username = form.data.get('username')
        photo_url = form.data.get('photo_url')
        print('Username:', username)
        print('Photo URL:', photo_url)
        username_exists = DragonUser.objects.filter(username=username).exists()
        print('Username exists?', username_exists)
        if username_exists:
            if username == user.username:
                return render(
                    request,
                    self.template_name,
                    {
                        'form': EditProfileForm(request.POST),
                        'error': 'That is already your username'
                    }
                )
            return render(
                request,
                self.template_name,
                {
                    'form': EditProfileForm(request.POST),
                    'error': 'That username is taken.'
                }
            )
        if username:
            user.username = username
        if photo_url:
            user.photo_url = photo_url
        user.save()
        print(user)
        return render(
            request,
            self.template_name,
            {
                'form': self.form,
                'message': 'Your changes have been saved!'
            }
        )


@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')


def homepage_view(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    return render(request, 'landing.html')


# testing here to move into character app


DND_API_URL = 'https://www.dnd5eapi.co/api/'


class NewCharacterView(View):
    form = CharacterTestForm()
    class_response = requests.get(DND_API_URL + 'classes/')
    class_data = class_response.json()['results']

    race_response = requests.get(DND_API_URL + 'races/')
    race_data = race_response.json()['results']

    test_char = {}

    def get(self, request):
        return render(
            request,
            'create.html',
            {
                'form': self.form,
                'classes': self.class_data,
                'races': self.race_data,
                'character': self.test_char,
            }
        )

    def post(self, request):
        form = CharacterTestForm(request.POST)
        data = request.POST.items()
        for field, data in data:
            print(field)
            print(data)
            print()
        return render(
            request,
            'create.html',
            {
                'form': form,
                'classes': self.class_data,
                'races': self.race_data,
                'character': request.POST,
            }
        )
