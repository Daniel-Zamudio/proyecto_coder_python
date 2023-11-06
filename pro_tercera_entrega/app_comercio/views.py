# from django.shortcuts import render
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from .models import Cliente


# class ListaClientes(ListView):
#     model = Cliente
#     context_object_name = 'clientes'

# class DetalleClientes(DetailView):
#     model = Cliente
    # context_object_name = 'clientes'


from django.shortcuts import render, redirect, HttpResponse
from .models import Articulo, Cliente, Proveedor, Venta
from .forms import ArticuloFormulario, ClienteFormulario, ProveedorFormulario, VentaFormulario


# Create your views here.

# def index(request):
#     return render(request, 'index.html')
def inicio(request):
    return render(request, "inicio.html")

def articulo_formulario(request):
    if request.method == "POST":
        mi_formulario_articulo = ArticuloFormulario(request.POST)

        if mi_formulario_articulo.is_valid():
            informacion_articulo = mi_formulario_articulo.cleaned_data
            nuevo_articulo = Articulo(
                                    nombre=informacion_articulo["nombre"],
                                    codigo=informacion_articulo["codigo"],
                                    precio=informacion_articulo["precio"],
                                    decripcion=informacion_articulo["decripcion"]
                                )
            nuevo_articulo.save()
            return redirect("inicio")
    else:
        mi_formulario_articulo = ArticuloFormulario()
        return render(request, "articulo_formulario.html", {"mi_formulario_articulo" : mi_formulario_articulo})

def cliente_formulario(request):
    if request.method == "POST":
        mi_formulario_cliente = ClienteFormulario(request.POST)
        
        if mi_formulario_cliente.is_valid():
            informacion_cliente = mi_formulario_cliente.cleaned_data
            nuevo_cliente = Cliente(
                            dni=informacion_cliente["dni"],
                            nombre=informacion_cliente["nombre"],
                            apellido=informacion_cliente["apellido"],
                            email=informacion_cliente["email"],
                            mayorista=informacion_cliente["mayorista"]
                            )
            nuevo_cliente.save()
            return redirect("inicio")
    else:
        mi_formulario_cliente = ClienteFormulario()
        return render(request, "cliente_formulario.html", {"mi_formulario_cliente" : mi_formulario_cliente})

def proveedor_formulario(request):
    if request.method == "POST":
        mi_formulario_proveedor = ProveedorFormulario(request.POST)
        
        if mi_formulario_proveedor.is_valid():
            informacion_proveedor = mi_formulario_proveedor.cleaned_data
            nuevo_profesor = Proveedor(
                            cuit=informacion_proveedor["cuit"],
                            razon_social=informacion_proveedor["razon_social"],
                            email=informacion_proveedor["email"]
                            )
            nuevo_profesor.save()
            return redirect("inicio")
    else:
        mi_formulario_proveedor = ProveedorFormulario()
        return render(request, "proveedor_formulario.html", {"mi_formulario_proveedor" : mi_formulario_proveedor})

def venta_formulario(request):
    if request.method == "POST":
        mi_formulario_venta = VentaFormulario(request.POST)
        
        if mi_formulario_venta.is_valid():
            informacion_venta = mi_formulario_venta.cleaned_data
            nueva_venta = Venta(
                            nombre_venta=informacion_venta["nombre_venta"],
                            dni_cliente=informacion_venta["dni_cliente"],
                            cuit_proveedor=informacion_venta["cuit_proveedor"],
                            monto=informacion_venta["monto"],
                            fecha=informacion_venta["fecha"])
            nueva_venta.save()
            return("inicio")
    else:
        mi_formulario_venta = VentaFormulario()
        return render(request, "venta_formulario.html", {"mi_formulario_venta" : mi_formulario_venta})

def buscar_articulo(request):
    # return render(request, "inicio.html")
    return render(request, "buscar_articulo.html")

def buscar(request):
    respuesta = f'Estoy buscando el articulo codigo: {request.GET["codigo"]}'
    if request.GET["codigo"]:
        codigo = request.GET["codigo"]
        nombres = Articulo.objects.filter(codigo__icontains=codigo)
        return render(request, "resultadosBusqueda.html", {"codigo" : codigo}, {"nombres" : nombres})
    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)



# def mostrar_fecha_actual(request):
#     fecha_actual = datetime.datetime.now()
#     return render(request, 'fecha_actual.html', {'fecha_actual': fecha_actual})

# def producto_list(request):
#     productos = Producto.objects.all()
#     print(productos)
#     return render(request, 'producto_list.html', {'productos': productos})

# def agregar_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             producto = form.save()
#             return redirect('CoderApp:index')  
#     else:
#         form = ProductoForm()
#     return render(request, 'producto_form.html', {'form': form})

