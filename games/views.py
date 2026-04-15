from django.views.generic import ListView, DetailView
from .models import Game, Tag

class GameReviewListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_name = self.request.GET.get('tag')
        if tag_name:
            queryset = queryset.filter(tags__name=tag_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'game'
        context['tags'] = Tag.objects.all()
        context['selected_tag'] = self.request.GET.get('tag', '')
        return context

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    context_object_name = 'game'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'game'
        return context

class TagListView(ListView):
    model = Tag
    template_name = 'games/tag_list.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'game'
        return context