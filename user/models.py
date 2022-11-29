from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nome
    class Meta:
        app_label = 'user'