
from django.urls import path
from finance.views import *
# from user.views import *
urlpatterns = [
    path('users_list/',users_list, name='users_list'),
    path('importcsv/', importcsv, name='importcsv'),
    path('detail_transacoes/<int:id>', detail_transacoes, name='detail_transacoes'),
    path('detailUser/<int:id>/',detailUser, name='detailUser'),
    path('removeUser/<int:id>/',removeUser, name='removeUser'),
]