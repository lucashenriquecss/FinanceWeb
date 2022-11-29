from django.contrib import admin
from .models import *
# Register your models here.
class ListandoUsers(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 5

admin.site.register(User,ListandoUsers)