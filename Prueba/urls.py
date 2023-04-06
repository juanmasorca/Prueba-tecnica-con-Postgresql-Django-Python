from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados/', views.empleados, name='empleados'),
    path('agregar_departamento/', views.agregar_departamento,
         name='agregar departamento'),
    path('departamentos/', views.departamentos,
         name='departamentos'),
]
