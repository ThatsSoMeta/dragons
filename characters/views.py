from django.shortcuts import render
from .forms import CharacterForm
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
            print('Data:', data)
        return render(
            request,
            'create.html',
            {
                'form': form,
            }
        )
