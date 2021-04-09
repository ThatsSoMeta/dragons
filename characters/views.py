from django.shortcuts import render
from .forms import CharacterForm
from .models import CharacterSheet
from django.views import View


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
        print(form.data)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print('Data:', data)
        return render(
            request,
            'create.html',
            {
                'form': form,
            }
        )


class CharacterDetailView(View):
    def get(self, request):
        template_name = 'character_detail.html'
        char = CharacterSheet.objects.all()
        print(char)
        context = {'char': char}
        return render(request, template_name, context)
