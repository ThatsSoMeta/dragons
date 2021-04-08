from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

class CharacterCreationView(View):
    form = CreateCharacterForm()
    template_name = 'generic_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form, 'header': 'Create Character'})
