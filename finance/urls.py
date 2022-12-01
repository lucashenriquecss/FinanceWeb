
from django.urls import path
from finance.views import *
# from user.views import *
urlpatterns = [
    path('users_list',users_list, name='users_list'),
    path('importcsv', importcsv, name='importcsv'),
]