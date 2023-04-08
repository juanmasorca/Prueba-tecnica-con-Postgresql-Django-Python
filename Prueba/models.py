#Importar Libertias a usar
from django.db import models
from django.db.models import Model

# Create your models here.

#Crear Tablas

# Define la clase Departamento para almacenar información sobre los departamentos
class departamento(models.Model):
    # Define el campo de código como un entero de 10 dígitos y llave primaria
    codigo = models.IntegerField(10, primary_key=True)
    # Define el campo de nombre como una cadena de hasta 100 caracteres
    nombre = models.CharField(max_length=100)
    # Define el campo de presupuesto como un número de punto flotante
    presupuesto = models.FloatField()

# Define la clase Empleado para almacenar información sobre los empleados
class Empleado(models.Model):
    # Define el campo de código como un entero de 10 dígitos y clave primaria
    codigo = models.IntegerField(10, primary_key=True)
    # Define el campo de NIF como una cadena de 9 caracteres
    nif = models.CharField(max_length=9)
    # Define el campo de nombre como una cadena de hasta 100 caracteres
    nombre = models.CharField(max_length=100)
    # Define el campo de apellido1 como una cadena de hasta 100 caracteres
    apellido1 = models.CharField(max_length=100)
    # Define el campo de apellido2 como una cadena de hasta 100 caracteres
    apellido2 = models.CharField(max_length=100)
    # Define el campo de código_departamento como una llave foránea a la clase Departamento
    codigo_departamento = models.ForeignKey(
        departamento, on_delete=models.CASCADE)
