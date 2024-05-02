from django.shortcuts import render
from .models import Factura

def search_form(request):
    return render(request, 'search_form.html')

def search_results(request):
    query = request.GET.get('query')
    results = Factura.objects.filter(nombre_cliente__icontains=query) # Esto es un ejemplo, ajusta según tus modelos y campos
    return render(request, 'search_results.html', {'results': results})
