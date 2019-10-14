from django.db import models
from datetime import datetime
# Create your models here.

class Juego(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio = models.IntegerField()
    clasificacion = models.CharField(max_length=50)
    stock = models.IntegerField()
    video = models.CharField(max_length=150,null=True)
    resenia = models.CharField(max_length=250)
    foto = models.ImageField(upload_to = "portadas/")
    PS3 = models.BooleanField(default = False)
    PS4 = models.BooleanField(default = False)
    XBOX360 = models.BooleanField(default = False)
    XBOXONE = models.BooleanField(default = False)
    NSWITCH = models.BooleanField(default = False)
    N3DS = models.BooleanField(default = False)
    PC = models.BooleanField(default = False)
    p = models.CharField(max_length=150)
    online = models.BooleanField(default = False)

class Comentario(models.Model):
    juego = models.IntegerField()
    comentario = models.CharField(max_length=150)
    usuario = models.CharField(max_length=70)
    creado = models.DateTimeField(default=datetime.now, blank=True)