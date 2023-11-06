from django.urls import path
# from . views import ListaClientes, DetalleClientes
from .  import views

urlpatterns = [
    # path('',ListaClientes.as_view(), name='articulos'),
    # path('cliente',DetalleClientes.as_view(), name='cliente')

    # path('fecha-actual/', views.mostrar_fecha_actual, name='mostrar_fecha_actual'),
    # path('productos/', views.producto_list, name='producto_list'),
    # path('index/', views.index, name='index'),
    # path('productos/agregar/', views.agregar_producto, name='agregar_producto'),

    path('', views.inicio, name= "inicio"),
    path('cliente/', views.cliente_formulario, name= "cliente_formulario"),
    path('proveedor/', views.proveedor_formulario, name= "proveedor_formulario"),
    path('articulo/', views.articulo_formulario, name= "articulo_formulario"),
    path('venta/', views.venta_formulario, name= "venta_formulario"),
    path('buscarArticulo/', views.buscar_articulo, name= "buscar_articulo"),
    path('buscar/', views.buscar, name= "buscar"),
]

