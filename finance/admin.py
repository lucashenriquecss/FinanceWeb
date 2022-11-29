from django.contrib import admin
from .models import *
# Register your models here.
class Transacoes(admin.ModelAdmin):#habilitando edição do admin 
    contaDestino = models.CharField(max_length=100, blank=False)
    contaDestino = models.CharField(max_length=100, blank=False)
    list_display = ('id', 'bancoorigem', 'agenciaorigem','contaorigem', 'bancodestino','agenciadestino','contadestino','valor','data')  
    list_display_links = ('id', 'bancoorigem')
    search_fields = ('bancoorigem',)
    list_filter = ('bancoorigem','bancodestino')
    list_per_page = 5
admin.site.register(Transacao)