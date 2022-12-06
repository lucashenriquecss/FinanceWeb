
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('finance/', include('finance.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('user.urls')),
]
