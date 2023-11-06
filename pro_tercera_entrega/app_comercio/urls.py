from django.urls import path
from .  import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('cliente/', views.cliente_formulario, name= "cliente_formulario"),
    path('proveedor/', views.proveedor_formulario, name= "proveedor_formulario"),
    path('articulo/', views.articulo_formulario, name= "articulo_formulario"),
    path('venta/', views.venta_formulario, name= "venta_formulario"),
    path('buscarArticulo/', views.buscar_articulo, name= "buscar_articulo"),
    path('buscar/', views.buscar, name= "buscar"),
]

