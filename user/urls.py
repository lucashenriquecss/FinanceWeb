
from django.urls import path

from user.views import *
urlpatterns = [
    path('home/',dashboard, name='dashboard'),
    path('', login, name='login'),
    path('', logout, name='logout'),
    path('registro/', registro, name='registro'),
    
]