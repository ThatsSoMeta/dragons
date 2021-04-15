from django.shortcuts import render, redirect, reverse
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
                background=data['background'],
                strength=data['strength'],
                dexterity=data['dexterity'],
                constitution=data['constitution'],
                intelligence=data['intelligence'],
                wisdom=data['wisdom'],
                charisma=data['charisma'],
            )
            print('Running get_attrs(new_char):')
            get_attrs(new_char)
        return redirect(reverse('view_characters'))


class CharacterDetailView(View):
    def get(self, request):
        template_name = 'char_view.html'
        char = Character.objects.all()
        context = {'char': char}
        return render(request, template_name, context)

