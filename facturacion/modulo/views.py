from django.shortcuts import render

def facturacion_view(request):
    return render(request, 'facturacion.html')

def productos_view(request):
    return render(request, 'productos.html')

def impuestos_view(request):
    return render(request, 'impuestos.html')

def informes_view(request):
    return render(request, 'informes.html')

def busqueda_view(request):
    return render(request, 'busqueda.html')

def empresa_view(request):
    return render(request, 'empresa.html')

def clientes_view(request):
    return render(request, 'clientes.html')
