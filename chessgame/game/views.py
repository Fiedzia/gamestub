import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
# Create your views here.
from .models import Game, GameMove


def new_game(request):
    #
    try:
        json_data = simplejson.loads(request.raw_post_data)
    except:
        raise HttpResponseServerError("Malformed data!")

    #get user1 and user2 from json_data
    #game = Game.new(user1, user2)
    #response = {
    #    'game_id': game.id
    #}
    
    return HttpResponse(json.dumps(response), content_type="application/json")

def cancel_game(request):
    pass

def make_move(request):
    #try:
    #    game = Game.objects.get(game_id)
    #    game.move(request.user, move_from, move_to)
    #except:
    #    raise HttpResponseServerError('Invalid move')
    #if game.is_finished():
    #   #this move won the game
    pass
