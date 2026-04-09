from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PhoneReview.urls')), # 把所有空的路径都交给 PhoneReview 处理
]