from wtforms import Form
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators


class UseForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('coreo')
    id=IntegerField('id')
    nombreProducto=StringField('nombreProducto')
    precio=StringField('precio')
    marca=StringField('marca')
    cantidad=StringField('cantidad')

class MateriaPrimaForm(Form):
    id=IntegerField('id')
    id_tipo=IntegerField('id_tipo')
    nombreMateriaPrima=StringField('nombreMateriaPrima')
    color=StringField('color')
    costo=StringField('costo')
    stock=StringField('stock')
    idProveedor=IntegerField('idProveedor')

class ProveedorForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    direccion=StringField('direccion')
    telefono=StringField('telefono')
    email=StringField('email')