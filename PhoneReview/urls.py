from django.urls import path
from . import views

urlpatterns = [
    # 添加手机型号（必须放在 <slug:slug>/ 之前）
    path('add-phone/', views.AddPhoneView.as_view(), name='add_phone'),
    # 添加测评文章（必须放在 <slug:slug>/ 之前）
    path('add-review/', views.AddReviewView.as_view(), name='add_review'),

    # 品牌列表页（独立路径，可选）
    path('brands/', views.BrandListView.as_view(), name='brand_list'),
    # 品牌下的型号列表页（使用品牌主键）
    path('brands/<int:pk>/', views.BrandPhoneModelListView.as_view(), name='brand_models'),
    # 型号详情页（使用型号主键）
    path('models/<int:pk>/', views.PhoneModelDetailView.as_view(), name='phonemodel_detail'),

    # 手机测评列表页（原首页迁移至此）
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),

    # 首页：显示所有品牌（满足老师要求）
    path('', views.BrandListView.as_view(), name='home'),

    # 测评详情页（使用 slug，注意必须放在最后，避免与 reviews/ 等冲突）
    path('<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),

    # 点赞/踩功能
    path('<slug:slug>/vote/<str:vote_type>/', views.review_vote, name='review_vote'),
]