from django.urls import path
from . import views

urlpatterns = [
    # 1. 首页：使用类视图 ReviewListView
    path('', views.ReviewListView.as_view(), name='review_list'),

    # 2. 详情页：使用类视图 ReviewDetailView
    # 注意：Django 会自动提取 <slug:slug> 并传递给 ReviewDetailView
    path('<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),

    # 3. 投票功能：保持不变，因为它在 views.py 中仍然是函数视图 (FBV)
    path('<slug:slug>/vote/<str:vote_type>/', views.review_vote, name='review_vote'),
]