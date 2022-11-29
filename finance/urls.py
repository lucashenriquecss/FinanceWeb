
from django.urls import path
from finance.views import *
urlpatterns = [
    path('importcsv', importcsv, name='importcsv'), 
]