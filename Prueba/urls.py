from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('empleados/', views.empleados, name='empleados'),

    path('agregar_empleado/', views.agregar_empleado, name='agregar empleado'),

    path('seleccionar_empleado/', views.seleccionar_empleado,
         name='seleccionar empleado'),

    path('seleccionar_empleado/<int:codigo>', views.editar_empleado,
         name='editar empleado'),

    path('eliminar_empleado/', views.vista_eliminar_empleado,
         name='vista eliminar empleado'),

    path('eliminar_empleado/<int:codigo>/',
         views.eliminar_empleado, name='eliminar empleado'),

    path('departamentos/', views.departamentos, name='departamentos'),

    path('agregar_departamento/', views.agregar_departamento,
         name='agregar departamento'),

    path('seleccionar_departamento/', views.seleccionar_departamento,
         name='seleccionar departamento'),

    path('seleccionar_departamento/<int:codigo>', views.editar_departamento,
         name='editar departamento'),

    path('eliminar_departamento/', views.vista_eliminar_departamento,
         name='vista eliminar departamento'),

    path('eliminar_departamento/<int:codigo>/',
         views.eliminar_departamento, name='eliminar departamento'),
]
