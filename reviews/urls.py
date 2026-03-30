from django.urls import path
from . import views

urlpatterns = [
    # 1. 首页：列出所有测评
    path('', views.review_list, name='review_list'),

    # 2. 详情页：查看单篇测评 + 提交评论 (由 views.review_detail 处理 POST)
    path('<slug:slug>/', views.review_detail, name='review_detail'),

    # 3. [新增] 投票功能：点击点赞或踩时跳转到这里处理数据，然后跳回详情页
    # <str:vote_type> 会匹配 url 里的 'like' 或 'dislike'
    path('<slug:slug>/vote/<str:vote_type>/', views.review_vote, name='review_vote'),
]