from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    fono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    ex_liceo = models.CharField(max_length=20)
    carrera = models.CharField(max_length=20)