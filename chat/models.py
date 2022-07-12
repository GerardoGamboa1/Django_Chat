from django.db import models
from datetime import datetime

# Create your models here.

class Canal(models.Model):
    nombre = models.CharField(max_length=250)

class Mensaje(models.Model):
    contenido = models.CharField(max_length=10000)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.CharField(max_length=250)
    canal = models.CharField(max_length=250)