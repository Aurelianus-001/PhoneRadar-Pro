from django.views.generic import ListView
from .models import Game

class GameReviewListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'