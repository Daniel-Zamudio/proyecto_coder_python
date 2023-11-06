from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mayorista = models.BooleanField(default=False)

    def __str__(self):
        return self.dni
    
    class Meta:
        ordering = ['apellido']

class Proveedor(models.Model):
    cuit = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mayorista = models.BooleanField(default=False)

    def __str__(self):
        return self.cuit
    
    class Meta:
        ordering = ['razon_social']

class Articulo(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=15)
    decripcion = models.TextField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.codigo
    
    class Meta:
        ordering = ['codigo']

class Venta(models.Model):
    codigo = models.CharField(max_length=6)
    codigo_articulo = models.CharField(max_length=15)
    cantidad = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return self.codigo
    
    class Meta:
        ordering = ['codigo']                