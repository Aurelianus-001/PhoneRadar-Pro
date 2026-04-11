from django.contrib import admin
from django.urls import path, include
from PhoneReview.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('index/', include('main.urls')),        # 确保这一行在下面一行之前
    path('', include('PhoneReview.urls')),       # 通配路由，放在最后
]