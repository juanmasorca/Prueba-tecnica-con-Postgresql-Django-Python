from django.shortcuts import render, redirect
from .models import departamento, Empleado


# Create your views here.

# Define una función llamada index que renderiza la plantilla 'index.html'
# cuando se recibe una solicitud GET en la URL asociada.
def index(request):
    return render(request, 'index.html')



# Define una función llamada departamentos que obtiene todos los objetos de la
# clase Departamento, los almacena en una lista y los pasa a la plantilla
# 'departamento/departamentos.html' como el contexto 'departamentos'.
def departamentos(request):
    # Obtener todos los objetos de la clase Departamento
    lista_departamentos = departamento.objects.all()
    #print(lista_departamentos)
    # Renderizar la plantilla 'departamento/departamentos.html' con la lista
    # de departamentos como el contexto 'departamentos'
    return render(request, 'departamento/departamentos.html', {'departamentos': lista_departamentos})



# Define una función llamada agregar_departamento que muestra un formulario para
# agregar un nuevo departamento si la solicitud es GET. Si la solicitud es POST,
# se crea un nuevo objeto Departamento con los datos proporcionados en el
# formulario y se guarda en la base de datos. Luego, se redirige al usuario a la
# misma página de agregar_departamento.
def agregar_departamento(request):
    if request.method == 'GET':
        # Si la solicitud es GET, mostrar el formulario de agregar departamento
        return render(request, 'departamento/agregar_departamento.html')
    else:
        # Si la solicitud es POST, crear un nuevo objeto Departamento con los
        # datos del formulario y guardarlo en la base de datos
        nuevo_departamento = departamento(
            codigo=request.POST['codigo'], nombre=request.POST['nombre'], presupuesto=request.POST['presupuesto'])
        nuevo_departamento.save()
        # Imprimir la información enviada en el formulario en la consola
        # print(request.POST)
        # Redirigir al usuario a la misma página de agregar_departamento
        return redirect('agregar departamento')



# Define una función llamada seleccionar_departamento que muestra una lista de
# todos los departamentos disponibles si la solicitud es GET. Si la solicitud
# es POST, se recupera el código del departamento seleccionado y se redirige al
# usuario a la página de edición de ese departamento.
def seleccionar_departamento(request):
    if request.method == 'GET':
        # Si la solicitud es GET, recuperar todos los departamentos disponibles
        lista_departamentos = departamento.objects.all()
        # Mostrar la lista de departamentos en la interfaz
        return render(request, 'departamento/seleccionar_departamento.html', {'departamentos': lista_departamentos})
    else:
        # Si la solicitud es POST, recuperar el código del departamento seleccionado
        codigo_departamento = request.POST['codigo']
        # Imprimir el código del departamento en la consola
        #print(codigo_departamento)
        # Redirigir al usuario a la página de edición del departamento seleccionado
        return redirect('editar departamento', codigo_departamento)



#Vista de editar Departamentos
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
            nombre=request.POST['nombre'], presupuesto=request.POST['presupuesto'])
        return redirect('seleccionar departamento')

#Vista de eliminar Departamentos
def vista_eliminar_departamento(request):
    if request.method == 'GET':
        lista_departamentos = departamento.objects.all()
        # sow interface
        return render(request, 'departamento/eliminar_departamento.html', {'departamentos': lista_departamentos})
    else:
        return redirect('vista eliminar departamento')

#Accion para eliminar de Departamentos
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
