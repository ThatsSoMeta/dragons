from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Game, GameNotes
from .forms import NewGameForm, NewGameNote


# Create your views here.
class UserGameListView(View):
    def get(self, request):
        user = request.user
        master = Game.objects.filter(gameMaster = user)
        player = Game.objects.filter(gamePlayers = user)
        return render(request, "user_game_list.html", {"user": user, "master": master, "player": player})

class GameDetailView(View):
    def get(self, request, game_id):
        game = Game.objects.get(gameID = game_id)
        notes = GameNotes.objects.filter(game = game).order_by('-createdAt')
        form = NewGameNote(initial={'game': game_id})
        return render(request, "game_detail.html", {"game": game, "notes": notes, "form": form})

    def post(self, request, game_id):
        form = NewGameNote(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            game = GameNotes.objects.create(
                game = Game.objects.get(gameID = game_id),
                body = data['body']
            )
        return redirect('game_details', game_id = game_id)

class NewGame(CreateView):

    def get(self, request):
        form = NewGameForm
        return render(request, "generic_form.html", {"form":form})

    def post(self, request):
        form = NewGameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            game = Game.objects.create(
                gameMaster = request.user,
                gameName = data['gameName']
            )
            game.gamePlayers.set(data['gamePlayers'])
        return redirect('game_list')

    