from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from game.models import Game


def create_game(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        game = Game.objects.create(player_one=player_name)
        return redirect('play_game', player_index=Game.PLAYER_ONE, game_code=str(game.code))
    return render(request, "game/index.html")


def join_game(request, game_code):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        game = get_object_or_404(Game, code=game_code)
        game.player_two = player_name
        game.save()
        return redirect('play_game', player_index=Game.PLAYER_TWO, game_code=str(game.code))
    ctx = {
        "is_join": True
    }
    return render(request, "game/index.html", ctx)


def play_game(request, player_index, game_code):
    game = Game.objects.get(code=game_code)

    if player_index == Game.PLAYER_TWO:
        game.start_date = timezone.now()
        game.save()
    ctx = {
        "game": game,
        "player_index": player_index
    }
    return render(request, "game/room.html", ctx)
