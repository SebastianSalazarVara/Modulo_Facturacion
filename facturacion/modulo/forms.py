from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Asegúrate de que está asociado al modelo correcto
        fields = ['dni', 'nombre', 'direccion', 'telefono', 'correo']  # Campos del formulario
