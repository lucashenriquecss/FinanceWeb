from django.urls import path
from user.views import *


urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('registro', registro, name='registro'),
]