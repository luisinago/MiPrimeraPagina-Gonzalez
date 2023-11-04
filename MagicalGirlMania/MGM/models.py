from django.db import models

#Campos clase Sailor Moon
class Sailor(models.Model):
    categoria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=10)
    planeta = models.CharField(max_length=50)
    objeto = models.CharField(max_length=20)

#Campos clase Winx
class Winx(models.Model):
     categoria = models.CharField(max_length=6)
     nombre = models.CharField(max_length=10)
     hada = models.CharField(max_length=50)
     transformacion = models.CharField(max_length=20)

#Campos clase Witch
class Witch(models.Model):
    categoria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=10)
    elemento = models.CharField(max_length=50)
    signo = models.CharField(max_length=20)