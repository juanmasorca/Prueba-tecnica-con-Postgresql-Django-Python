from django.shortcuts import render, redirect
from .models import departamento, Empleado


# Create your views here.


def index(request):
    return render(request, 'index.html')


def departamentos(request):
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    lista_departamentos = departamento.objects.all()
    print(lista_departamentos)
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


def seleccionar_departamento(request):
    if request.method == 'GET':
        lista_departamentos = departamento.objects.all()
        # sow interface
        return render(request, 'departamento/seleccionar_departamento.html', {'departamentos': lista_departamentos})
    else:
        codigo_departamento = request.POST['codigo']
        print(codigo_departamento)
        return redirect('editar departamento', codigo_departamento)


def editar_departamento(request, codigo):
    if request.method == 'GET':
        lista_departamentos = departamento.objects.get(codigo=codigo)
        print(lista_departamentos.nombre)
        # show interface
        return render(request, 'departamento/editar_departamento.html', {'departamentos': lista_departamentos})
    else:
        # Datos = departamento.objects.get(codigo=codigo)
        print(request.POST)
        departamento.objects.filter(codigo=request.POST['codigo']).update(
            nombre=request.POST['nombre'])
        return redirect('seleccionar departamento')


def vista_eliminar_departamento(request):
    if request.method == 'GET':
        lista_departamentos = departamento.objects.all()
        # sow interface
        return render(request, 'departamento/eliminar_departamento.html', {'departamentos': lista_departamentos})
    else:
        return redirect('vista eliminar departamento')


def eliminar_departamento(request, codigo):
    departamento_a_eliminar = departamento.objects.get(codigo=codigo)
    print(departamento_a_eliminar.nombre)
    departamento_a_eliminar.delete()
    return redirect('vista eliminar departamento')


def empleados(request):
    lista_empleados = Empleado.objects.all()

    return render(request, 'empleados/empleados.html', {'empleados': lista_empleados})


def agregar_empleado(request):
    if request.method == 'GET':
        # sow interface
        lista_departamentos = departamento.objects.all()
        return render(request, 'empleados/agregar_empleado.html', {'departamentos': lista_departamentos})
    else:
        nuevo_empleado = Empleado(codigo=request.POST['codigo'], nif=request.POST['nif'], nombre=request.POST['nombre'],
                                  apellido1=request.POST['apellido1'], apellido2=request.POST['apellido2'], codigo_departamento_id=request.POST['departamento'])
        nuevo_empleado.save()
        print(request.POST)
        return redirect('agregar empleado')


def seleccionar_empleado(request):
    if request.method == 'GET':
        lista_empleados = Empleado.objects.all()
        # sow interface
        return render(request, 'empleados/seleccionar_empleado.html', {'empleados': lista_empleados})
    else:
        print(request.POST)
        codigo_empleado = request.POST['codigo']
        return redirect('editar empleado', codigo_empleado)


def editar_empleado(request, codigo):
    if request.method == 'GET':
        lista_departamentos = departamento.objects.all()
        codigo_empleado = Empleado.objects.get(codigo=codigo)
        print(codigo_empleado.nombre)
        # show interface
        return render(request, 'empleados/editar_empleado.html', {'empleados': codigo_empleado, 'departamentos': lista_departamentos})
    else:
        # Datos = departamento.objects.get(codigo=codigo)
        Empleado.objects.filter(codigo=request.POST['codigo']).update(nif=request.POST['nif'], nombre=request.POST['nombre'],
                                                                      apellido1=request.POST['apellido1'], apellido2=request.POST['apellido2'], codigo_departamento_id=request.POST['departamento'])
        print(request.POST)
        # departamento.objects.filter(codigo=request.POST['codigo']).update(
        # nombre=request.POST['nombre'])
        return redirect('seleccionar empleado')


def vista_eliminar_empleado(request):
    if request.method == 'GET':
        lista_empleados = Empleado.objects.all()
        # sow interface
        return render(request, 'empleados/eliminar_empleados.html', {'empleados': lista_empleados})
    else:
        return redirect('vista eliminar empleado')


def eliminar_empleado(request, codigo):
    empleado_a_eliminar = Empleado.objects.get(codigo=codigo)
    print(empleado_a_eliminar.nombre)
    empleado_a_eliminar.delete()
    return redirect('vista eliminar empleado')
