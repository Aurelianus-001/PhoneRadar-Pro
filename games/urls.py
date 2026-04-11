from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameReviewListView.as_view(), name='game_list'),
]