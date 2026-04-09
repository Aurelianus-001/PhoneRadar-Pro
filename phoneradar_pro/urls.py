from django.contrib import admin
from django.urls import path, include
from PhoneReview.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('PhoneReview.urls')),
]