from django.shortcuts import render
from django.views import View
from .forms import CharacterForm
from .models import Character


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
            print(data)
            new_char = Character.objects.create(
                name=data['name'],
                player=request.user,
                class_name=data['class_name'],
                race=data['race'],
                alignment=data['alignment'],
            )
            print(new_char)
        return render(
            request,
            'create.html',
            {
                'form': form,
                'message': 'Your character has been saved.'
            }
        )
