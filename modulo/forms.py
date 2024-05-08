from django import forms
from .models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Asegúrate de que está asociado al modelo correcto
        fields = ['dni', 'nombre', 'direccion', 'telefono', 'correo']  # Campos del formulario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'stock']  # Campos del formulario
