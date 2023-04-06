from django.shortcuts import render, redirect
from .models import departamento

# Create your views here.


def index(request):
    return render(request, 'index.html')


def empleados(request):
    return render(request, 'empleados/empleados.html')


def agregar_empleado(request):
    return redirect(request, )


def departamentos(request):
    lista_departamentos = departamento.objects.all()

    return render(request, 'departamento/departamentos.html', {'departamentos': lista_departamentos})


def agregar_departamento(request):
    if request.method == 'GET':
        # sow interface
        return render(request, 'departamento/agregar_departamento.html')
    else:
        nuevo_departamento = departamento(
            codigo=request.POST['codigo'], nombre=request.POST['nombre'], presupuesto=request.POST['presupuesto'])
        nuevo_departamento.save()
        # print(request.POST)
        return redirect('agregar departamento')
