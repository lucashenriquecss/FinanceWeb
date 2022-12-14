from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Transacao(models.Model):
    bancoorigem = models.CharField(max_length=100, blank=False)
    agenciaorigem = models.CharField(max_length=100, blank=False)
    contaorigem = models.CharField(max_length=100, blank=False)
    bancodestino = models.CharField(max_length=100, blank=False)
    agenciadestino = models.CharField(max_length=100, blank=False)
    contadestino = models.CharField(max_length=100, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(blank=False)
    impor = models.DateField(default=datetime.now,blank=False)
    usuario = models.ForeignKey(User,on_delete=CASCADE,null=True)

    def __str__(self):
        return self.bancoorigem,self.bancodestino,self.data,self.usuario