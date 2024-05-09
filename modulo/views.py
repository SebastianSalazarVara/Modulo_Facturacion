from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Cliente, Empresa, Producto  # Importar el modelo Cliente
from .forms import ClienteForm, EmpresaForm, ProductoForm  # Importar el formulario Cliente

def facturacion_view(request):    
    return render(request, 'facturacion.html')


def productos_view(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Producto guardado")
            return redirect('productos')
        else:
            print("Errores de validación:", form.errors)
    else:
        form = ProductoForm()
    productos = Producto.objects.all()
    return render(request, 'productos.html', {
        'form': form,
        'productos': productos,
    })

def impuestos_view(request):
    return render(request, 'impuestos.html')

def informes_view(request):
    return render(request, 'informes.html')

def busqueda_view(request):
    return render(request, 'busqueda.html')

def empresa_view(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            empresa = Empresa.objects.first()
            if 'imagen' in request.FILES:
                empresa.imagen = request.FILES['imagen']
            empresa.nombre = form.cleaned_data['nombre']
            empresa.direccion = form.cleaned_data['direccion']
            empresa.telefono = form.cleaned_data['telefono']
            empresa.save()
            print("Empresa Actualizada")
            return redirect('empresa')
        else:
            print("Errores de validación:", form.errors)
    else:
        #formEmpresa= EmpresaForm(Empresa.objects.first())
        empresa= Empresa.objects.first()
        print(empresa)
    return render(request, 'empresa.html', {
        'empresa': empresa,
    })

def clientes_view(request):
    if request.method == "POST":  # Cuando se envía el formulario
        form = ClienteForm(request.POST)
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar el cliente
            print("Cliente guardado")  # Confirmación de guardado
            return redirect('clientes')  # Redirigir a la misma vista
        else:
            print("Errores de validación:", form.errors)  # Mostrar errores de validación
    else:
        form = ClienteForm()  # Para solicitudes GET o si el formulario no es válido

    # Obtener todos los clientes para mostrar en la tabla
    clientes = Cliente.objects.all()

    return render(request, 'clientes.html', {
        'form': form,  # El formulario para agregar nuevos clientes
        'clientes': clientes,  # La lista de clientes para mostrar en la tabla
    })

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Obtener el cliente por ID
    if request.method == "POST":  # Si se envía el formulario
        form = ClienteForm(request.POST, instance=cliente)  # Formulario pre-rellenado
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar cambios
            return redirect('clientes')  # Redirigir a la lista de clientes
    else:  # Si es GET, mostrar el formulario con datos existentes
        form = ClienteForm(instance=cliente)
        # Deshabilitar ciertos campos
        form.fields['dni'].widget.attrs['readonly'] = True
        form.fields['nombre'].widget.attrs['readonly'] = True

    # Añadir a los datos de contexto información adicional
    return render(request, 'clientes.html', {
        'form': form,  # Formulario para editar cliente
        'clientes': Cliente.objects.all(),  # Lista de clientes para mostrar
        'editar_cliente': True  # Bandera para mostrar botones adicionales
    })

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Obtener el cliente o mostrar 404 si no se encuentra
    cliente.delete()  # Eliminar el cliente de la base de datos
    return redirect('clientes')  # Redirigir a la lista de clientes


# def agregar_producto(request):
#     if request.method == "POST":
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Producto guardado")
#             return redirect('productos')
#         else:
#             print("Errores de validación:", form.errors)
#     else:
#         form = ProductoForm()

#     productos = Producto.objects.all()

#     return render(request, 'productos.html', {
#         'form': form,
#         'productos': productos,
#     })

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos.html', {
        'form': form,
        'productos': Producto.objects.all(),
        'editar_producto': True
    })

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('productos')

