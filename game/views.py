from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
from .models import (
    Game,
    GameNotes,
    ActionRequest,
    # PlayerAction,
    Narrative
)
from .forms import (
    NewGameForm,
    NewGameNote,
    NarrativeForm,
    PlayerActionForm,
    ActionRequestForm
)
from characters.models import Character


# Create your views here.
class UserGameListView(View):
    def get(self, request):
        user = request.user
        master = Game.objects.filter(gameMaster=user)
        player = Game.objects.filter(gamePlayers=user)
        return render(
            request,
            "user_game_list.html",
            {
                "user": user,
                "master": master,
                "player": player
            }
        )


class GameDetailView(View):
    def get(self, request, game_id):
        game = Game.objects.get(gameID=game_id)
        notes = GameNotes.objects.filter(game=game).order_by('-createdAt')
        note_form = NewGameNote(initial={'game': game_id})
        action_requests = ActionRequest.objects.filter(game=game)
        action_request_form = ActionRequestForm()
        narrative_items = Narrative.objects.filter(game=game)
        narrative_form = NarrativeForm()
        player_action_form = PlayerActionForm()
        character = None
        if game.gameMaster != request.user:
            character_query = Character.objects.filter(
                gameID=game_id,
                player=request.user
            )
            if character_query.count:
                character = character_query.first()
        player_characters = Character.objects.filter(player=request.user, gameID=None)
        return render(
            request,
            "game_detail.html",
            {
                "game": game,
                "notes": notes,
                "note_form": note_form,
                "action_request_form": action_request_form,
                "action_requests": action_requests,
                "narrative_form": narrative_form,
                "narrative_items": narrative_items,
                "player_action_form": player_action_form,
                "character": character,
                "player_characters": player_characters,
            }
        )

    def post(self, request, game_id):
        game = Game.objects.get(gameID=game_id)
        note_form = NewGameNote(request.POST)
        narrative_form = NarrativeForm(request.POST)
        action_request_form = ActionRequestForm(request.POST)
        character = None
        if game.gameMaster != request.user:
            character_query = Character.objects.filter(
                gameID=game_id,
                player=request.user
            )
            if character_query.count:
                character = character_query.first()
        if request.user == game.gameMaster:
            if note_form.is_valid():
                note_data = note_form.cleaned_data
                game = GameNotes.objects.create(
                    game=Game.objects.get(gameID=game_id),
                    body=note_data['body']
                )
                print(game)
            if narrative_form.is_valid():
                narrative_data = narrative_form.cleaned_data
                Narrative.objects.create(
                    game=game,
                    text=narrative_data['text']
                )
        else:
            if action_request_form.is_valid():
                action_request_data = action_request_form.cleaned_data
                ActionRequest.objects.create(
                    game=game,
                    player=request.user,
                    character=character,
                    text=action_request_data['text']
                )
        return redirect('game_details', game_id=game_id)


class NewGame(CreateView):

    def get(self, request):
        form = NewGameForm
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = NewGameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            game = Game.objects.create(
                gameMaster=request.user,
                gameName=data['gameName']
            )
            game.gamePlayers.set(data['gamePlayers'])
        return redirect('game_list')


def select_character(request, game_id, char_id):
    character = Character.objects.get(id=char_id)
    game = Game.objects.get(gameID=game_id)
    character.gameID = game.gameID
    character.is_active = True
    character.save()
    return redirect(reverse('game_details', args=[game_id]))
