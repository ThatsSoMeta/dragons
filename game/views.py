from django.shortcuts import render, redirect, reverse
from django.views import View
# from django.db.models import Q
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
from .models import (
    Game,
    GameNotes,
    ActionRequest,
    PlayerAction,
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
        action_requests = PlayerAction.objects.filter(
            game=game,
            status=PlayerAction.PENDING
        )
        action_request_form = ActionRequestForm()
        narrative_items = Narrative.objects.filter(game=game)
        narrative_form = NarrativeForm()
        player_action_form = PlayerActionForm()
        character = None
        # skill_checks = None
        skill_checks = PlayerAction.objects.filter(
            game=game,
            status=PlayerAction.ACCEPTED,
            completed=False,
        )
        if game.gameMaster != request.user:
            character_query = Character.objects.filter(
                gameID=game_id,
                player=request.user
            )
            if character_query.count:
                character = character_query.first()
        player_characters = Character.objects.filter(
            player=request.user,
            gameID=None
        )
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
                "skill_checks": skill_checks,
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
                req_character = Character.objects.get(
                    player=request.user,
                    gameID=game.gameID
                )
                PlayerAction.objects.create(
                    game=game,
                    requested_by=request.user,
                    status=PlayerAction.PENDING,
                    action_text=action_request_data['text'],
                    player_character=req_character
                )
        return redirect('game_details', game_id=game_id)


class NewGame(View):

    def get(self, request):
        form = NewGameForm()
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
        return redirect('homepage')


def select_character(request, game_id, char_id):
    character = Character.objects.get(id=char_id)
    game = Game.objects.get(gameID=game_id)
    character.gameID = game.gameID
    character.is_active = True
    character.save()
    return redirect(reverse('game_details', args=[game_id]))


def reject_action(request, action_id, game_id):
    action = PlayerAction.objects.get(id=action_id)
    action.status = action.REJECTED
    action.save()
    return redirect(reverse('game_details', args=[game_id]))


class AcceptAction(View):
    def get(self, request, game_id, action_id):
        action = PlayerAction.objects.get(id=action_id)
        game = action.game
        character_options = Character.objects.filter(gameID=game_id)
        form = PlayerActionForm()
        return render(
            request,
            'action.html',
            {
                'form': form,
                'action': action,
                'game': game,
                'character_options': character_options,
            }
        )

    def post(self, request, game_id, action_id):
        action = PlayerAction.objects.get(id=action_id)
        game = action.game
        form = PlayerActionForm(request.POST)
        print('Action is accepted')
        print('checking entries:')
        for entry in form.data['char_name']:
            char = Character.objects.get(id=entry)
            print('Adding character:', char.name)
            action.characters.add(char)
            action.save()
        action.related_skill = form.data.get('related_skill')[0]
        action.status = action.ACCEPTED
        action.save()
        print('Action characters:')
        for option in action.characters.all():
            print(option.name)
        return redirect(
            reverse('game_details', args=[game.gameID])
        )
