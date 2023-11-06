from django.contrib import admin
from .models import Cliente, Proveedor, Articulo, Venta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Articulo)
admin.site.register(Venta)
