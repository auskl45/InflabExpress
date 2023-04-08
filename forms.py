from wtforms import Form
from wtforms import StringField,IntegerField,FloatField,DateField,DateTimeField,BooleanField,SelectField,TextAreaField,PasswordField,FileField
from wtforms import EmailField
from wtforms import validators


class UseForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('coreo')


class ProductoForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    descripcion=TextAreaField('descripcion')
    stock=IntegerField('stock')
    altura=FloatField('altura')
    ancho=FloatField('ancho')
    largo=FloatField('largo')
    image=FileField('image')
    subtotal=FloatField('subtotal')
    total=FloatField('total')

class MateriaPrimaForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    color=StringField('color')
    costo=FloatField('costo')
    stock=FloatField('stock')
    tipoMateriaPrima_id=IntegerField('tipoMateriaPrima_id')
    proveedor_id=IntegerField('proveedor_id')

class TipoMateriaPrimaForm(Form):
    id=IntegerField('id')
    tipo=StringField('tipo')
    UnidadMedida=StringField('UnidadMedida')

class GastoMateriaPrimaForm(Form):
    id=IntegerField('id')
    cantidad=FloatField('cantidad')
    total=FloatField('total')
    fecha=DateField('fecha')
    materiaPrima_id=IntegerField('materiaPrima_id')
    producto_id=IntegerField('producto_id')


"""class Producto(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    stock = db.Column(db.Integer())
    altura = db.Column(db.Float())
    ancho = db.Column(db.Float())
    largo = db.Column(db.Float())
    image = db.Column(db.Text, nullable=False)
    subtotal = db.Column(db.Float())
    total = db.Column(db.Float())
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    productoGastoMateria = db.relationship('GastoMateriaPrima', backref='producto', lazy='dynamic')
    productoPedido = db.relationship('Pedido', backref='producto', lazy='dynamic')"""