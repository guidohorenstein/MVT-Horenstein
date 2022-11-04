from django.db import models
from datetime import datetime


# Create your models here.
class Familia(models.Model):
    parentesco = models.CharField(max_length=50)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateTimeField()


    #nombre = models.CharField(max_length=40)
    #apellido = models.CharField(max_length=40)
    #parentesco = models.CharField(max_length=40)
    #edad = models.IntegerField()
    #fecha_nacimiento = models.DateTimeField()
    

