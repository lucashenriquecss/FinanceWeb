
from django.urls import path
from finance.views import *
urlpatterns = [
    path('', index, name='index'),
    #path('import/csv/impressora', import_csv, name='import_csv'),
    
]