from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=8, unique=True)  # Identificador único
    nombre = models.CharField(max_length=100)  # Nombre del cliente
    direccion = models.CharField(max_length=255, blank=True, null=True)  # Dirección (opcional)
    telefono = models.CharField(max_length=9, blank=True, null=True)  # Teléfono (opcional)
    correo = models.EmailField(blank=True, null=True)  # Correo electrónico (opcional)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)  # Código único
    nombre = models.CharField(max_length=100)  # Nombre del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    stock = models.PositiveIntegerField()  # Cantidad en stock

    def __str__(self):
        return f"{self.nombre} (${self.precio})"