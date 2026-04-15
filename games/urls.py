from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.TagListView.as_view(), name='tag_list'),  # 具体路径放在前面
    path('', views.GameReviewListView.as_view(), name='game_list'),
    path('<slug:slug>/', views.GameDetailView.as_view(), name='game_detail'),
]