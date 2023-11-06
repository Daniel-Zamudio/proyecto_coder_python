from django import forms


class ArticuloFormulario(forms.Form):
    codigo = forms.CharField(max_length=6)
    nombre = forms.CharField()
    precio = forms.FloatField()
    decripcion = forms.CharField()

class ClienteFormulario(forms.Form):
    dni= forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    mayorista = forms.BooleanField()

class ProveedorFormulario(forms.Form):
    cuit= forms.CharField()
    razon_social = forms.CharField()
    email = forms.EmailField()
    domicilio = forms.CharField()
    telefono = forms.CharField()
    mayorista = forms.BooleanField()


class VentaFormulario(forms.Form):
    codigo = forms.CharField(max_length=6)
    codigo_articulo = forms.CharField(max_length=15)
    cantidad = forms.IntegerField()
    total = forms.FloatField()