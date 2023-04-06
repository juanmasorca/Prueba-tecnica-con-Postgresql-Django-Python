from django.db import models
from django.db.models import Model

# Create your models here.


class departamento(models.Model):
    codigo = models.IntegerField(10, primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()


class Empleado(models.Model):
    codigo = models.IntegerField(10, primary_key=True)
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey(
        departamento, on_delete=models.CASCADE)
