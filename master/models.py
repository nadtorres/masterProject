from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class registrar(models.Model):
    email = models.EmailField();
    nombreUsuario = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=35)
    apellidoPaterno= models.CharField(max_length=35)
    apellidoMaterno= models.CharField(max_length=35)
    rut=models.CharField(max_length=9)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreUsuario