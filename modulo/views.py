from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Cliente, Producto  # Importar el modelo Cliente
from .forms import ClienteForm, ProductoForm  # Importar el formulario Cliente

def facturacion_view(request):
    producto_encontrado = None
    if request.method == "POST":
        codigo_producto = request.POST.get('codigo_producto')
        try:
            producto_encontrado = Producto.objects.get(codigo=codigo_producto)
        except Producto.DoesNotExist:
            pass
    return render(request, 'facturacion.html', {'producto_encontrado': producto_encontrado})


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
    return render(request, 'empresa.html')

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

def buscar_producto(request):
    codigo_producto = request.GET.get('codigo_producto', None)
    if codigo_producto:
        try:
            producto = Producto.objects.get(codigo=codigo_producto)
            data = {
                'nombre': producto.nombre,
                'precio': producto.precio
            }
            return JsonResponse(data)
        except Producto.DoesNotExist:
            pass
    return JsonResponse({'error': 'Producto no encontrado'}, status=404)
