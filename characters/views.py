from django.shortcuts import render
from django.views import View
from .forms import CharacterForm
from .models import Character
from .helpers import get_attrs


# Create your views here.


class NewCharacterView(View):
    form = CharacterForm()

    def get(self, request):
        return render(
            request,
            'create.html',
            {
                'form': self.form,
            }
        )

    def post(self, request):
        form = CharacterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_char = Character.objects.create(
                name=data['name'],
                player=request.user,
                class_name=data['class_name'],
                race=data['race'],
                alignment=data['alignment'],
            )
            print('Running get_attrs(new_char):')
            get_attrs(new_char)
        return render(
            request,
            'create.html',
            {
                'form': form,
            }
        )
