from django.urls import path
from . import views

urlpatterns = [
    # 添加手机型号（必须放在 <slug:slug>/ 之前）
    path('add-phone/', views.AddPhoneView.as_view(), name='add_phone'),
    # 添加测评文章（必须放在 <slug:slug>/ 之前）
    path('add-review/', views.AddReviewView.as_view(), name='add_review'),

    # 1. 首页：使用类视图 ReviewListView
    path('', views.ReviewListView.as_view(), name='review_list'),

    # 2. 详情页：使用类视图 ReviewDetailView
    path('<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),

    # 3. 投票功能：函数视图
    path('<slug:slug>/vote/<str:vote_type>/', views.review_vote, name='review_vote'),
]