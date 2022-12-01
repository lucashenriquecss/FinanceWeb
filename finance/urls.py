
from django.urls import path
from finance.views import *
# from user.views import *
urlpatterns = [
    # path('home',dashboard, name='dashboard'),
    # path('', login, name='login'),
    # path('registro/', registro, name='registro'),
    path('importcsv', importcsv, name='importcsv'),
]