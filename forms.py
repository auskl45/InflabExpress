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
    nombre=StringField('nombre', [validators.DataRequired(message='El nombre es requerido'), validators.length(min=4, max=255, message='El nombre debe ser mayor a 4 caracteres')])
    descripcion=TextAreaField('descripcion', [validators.DataRequired(message='La descripcion es requerida'), validators.length(min=4, message='La descripcion debe ser mayor a 4 caracteres')])
    stock=IntegerField('stock', [validators.DataRequired(message='El stock es requerido'), validators.number_range(min=0 , message='El stock debe ser mayor a 0')])
    altura=FloatField('altura', [validators.DataRequired(message='La altura es requerida'), validators.number_range(min=0 , message='La altura debe ser mayor a 0')])
    ancho=FloatField('ancho', [validators.DataRequired(message='El ancho es requerido'), validators.number_range(min=0 , message='El ancho debe ser mayor a 0')])
    largo=FloatField('largo', [validators.DataRequired(message='El largo es requerido'), validators.number_range(min=0 , message='El largo debe ser mayor a 0')])
    image=FileField('image', [validators.DataRequired(message='La imagen es requerida')])
    subtotal=FloatField('subtotal', [validators.DataRequired(message='El subtotal es requerido'), validators.number_range(min=0 , message='El subtotal debe ser mayor a 0')])
    total=FloatField('total', [validators.DataRequired(message='El total es requerido'), validators.number_range(min=0 , message='El total debe ser mayor a 0')])

class MateriaPrimaForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre', [validators.DataRequired(message='El nombre es requerido'), validators.length(min=4, max=255, message='El nombre debe ser mayor a 4 caracteres')])
    costo=FloatField('costo', [validators.DataRequired(message='El costo es requerido'), validators.number_range(min=0 , message='El costo debe ser mayor a 0')])
    stock=FloatField('stock', [validators.DataRequired(message='El stock es requerido'), validators.number_range(min=0 , message='El stock debe ser mayor a 0')])
    tipoMateriaPrima_id=IntegerField('tipoMateriaPrima_id', [validators.DataRequired(message='Seleccione el tipo de materia prima')])
    proveedor_id=IntegerField('proveedor_id', [validators.DataRequired(message='Seleccione el proveedor')])

class TipoMateriaPrimaForm(Form):
    id=IntegerField('id')
    tipo=StringField('tipo', [validators.DataRequired(message='El tipo es requerido'), validators.length(min=4, max=255, message='El tipo de materia debe ser mayor a 4 caracteres')])
    UnidadMedida=StringField('UnidadMedida', [validators.DataRequired(message='La unidad de medida es requerida'), validators.length(min=4, max=255, message='La unidad de medida debe ser mayor a 4 caracteres')])

class GastoMateriaPrimaForm(Form):
    id=IntegerField('id')
    cantidad=FloatField('cantidad', [validators.DataRequired(message='La cantidad es requerida'), validators.length(min=0 , message='La cantidad debe ser mayor a 0')])
    total=FloatField('total', [validators.DataRequired(message='El total es requerido'), validators.number_range(min=0 , message='El total debe ser mayor a 0')])
    materiaPrima_id=IntegerField('materiaPrima_id', [validators.DataRequired(message='Seleccione la materia prima')])
    producto_id=IntegerField('producto_id', [validators.DataRequired(message='Seleccione el producto')])


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