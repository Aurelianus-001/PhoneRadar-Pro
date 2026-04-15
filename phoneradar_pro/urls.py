from django.contrib import admin
from django.urls import path, include
from PhoneReview.views import RegisterView, HomeView, BrandListView, AllPhoneModelListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('index/', include('main.urls')),
    path('games/', include('games.urls')),

    # 首页（网站介绍）
    path('', HomeView.as_view(), name='home'),

    # 手机品牌、型号相关
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('models/', AllPhoneModelListView.as_view(), name='all_models'),

    # 其他 PhoneReview 路由（包含 add-phone, add-review, 测评列表, 详情等）
    path('', include('PhoneReview.urls')),
]