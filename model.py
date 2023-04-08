from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_security import UserMixin, RoleMixin,SQLAlchemyUserDatastore

db=SQLAlchemy()


# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

"""class Alumnos(db.Model):
    __tablename__='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(100))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)"""

"""class Maestros(db.Model):
    __tablename__='maestros'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(100))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)"""

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    userPedido = db.relationship('Pedido', backref='user', lazy='dynamic')
    

class Venta(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    deuda = db.Column(db.Float())
    fechaVenta = db.Column(db.DateTime(),default=datetime.datetime.now)
    estatusVenta = db.Column(db.String(255))
    pedido_id = db.Column(db.Integer(), db.ForeignKey('pedido.id'))

class Pedido(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cantidad = db.Column(db.Float())
    Totalprecio = db.Column(db.Float())
    anticipo = db.Column(db.Float())
    estatusPedido = db.Column(db.String(255))
    fechaCreacion = db.Column(db.DateTime(),default=datetime.datetime.now)
    producto_id = db.Column(db.Integer(), db.ForeignKey('producto.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    pedidoVenta = db.relationship('Venta', backref='pedido', lazy='dynamic')

class Producto(db.Model, RoleMixin):
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
    productoPedido = db.relationship('Pedido', backref='producto', lazy='dynamic')

class TipoMateriaPrima(db.Model):
    __tablename__='tipomateriaprima'
    id = db.Column(db.Integer(), primary_key=True)
    tipo = db.Column(db.String(255))
    UnidadMedida = db.Column(db.String(255))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    tipoMateriaPrima = db.relationship('MateriaPrima', backref='tipoMateriaPrima', lazy='dynamic')

class MateriaPrima(db.Model):
    __tablename__='materiaprima'
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    color = db.Column(db.String(255))
    costo = db.Column(db.Float())
    stock = db.Column(db.Float())
    tipoMateriaPrima_id = db.Column(db.Integer(), db.ForeignKey('tipomateriaprima.id'))
    proveedor_id = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))
    materiaPrimaCompra = db.relationship('Compra', backref='materiaPrima', lazy='dynamic')
    materiaPrimaGasto = db.relationship('GastoMateriaPrima', backref='materiaPrima', lazy='dynamic')

class Compra(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cantidad = db.Column(db.Float())
    total = db.Column(db.Float())
    fecha = db.Column(db.DateTime(),default=datetime.datetime.now)
    materiaPrima_id = db.Column(db.Integer(), db.ForeignKey('materiaprima.id'))
    proveedor_id = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))

class GastoMateriaPrima(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cantidad = db.Column(db.Float())
    costo = db.Column(db.Float())
    materiaPrima_id = db.Column(db.Integer(), db.ForeignKey('materiaprima.id'))
    producto_id = db.Column(db.Integer(), db.ForeignKey('producto.id'))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)


class Proveedor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.Integer())
    email = db.Column(db.String(255))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    proveedorCompra = db.relationship('Compra', backref='proveedor', lazy='dynamic')
    proveedorMateria = db.relationship('MateriaPrima', backref='proveedor', lazy='dynamic')

"""class Proveedor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.Integer())
    email = db.Column(db.String(255))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    proveedorCompra = db.relationship('Compra', backref='proveedor', lazy='dynamic')
    proveedorMateria = db.relationship('MateriaPrima', backref='proveedor', lazy='dynamic')




class TipoMateriaPrima(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    tipo = db.Column(db.String(255))
    UnidadMedida = db.Column(db.String(255))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    tipoMateriaPrima = db.relationship('MateriaPrima', backref='tipoMateriaPrima', lazy='dynamic')


class MateriaPrima(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    color = db.Column(db.String(255))
    costo = db.Column(db.Float())
    stock = db.Column(db.Float())
    tipoMateriaPrima_id = db.Column(db.Integer(), db.ForeignKey('tipomateriaprima.id'))
    proveedor_id = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))
    materiaPrimaCompra = db.relationship('Compra', backref='materiaPrima', lazy='dynamic')
    materiaPrimaGasto = db.relationship('GastoMateriaPrima', backref='materiaPrima', lazy='dynamic')


class Compra(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cantidad = db.Column(db.Float())
    total = db.Column(db.Float())
    fecha = db.Column(db.DateTime(),default=datetime.datetime.now)
    materiaPrima_id = db.Column(db.Integer(), db.ForeignKey('materiaprima.id'))
    proveedor_id = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))





class Producto(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    stock = db.Column(db.Integer())
    altura = db.Column(db.Float())
    ancho = db.Column(db.Float())
    largo = db.Column(db.Float())
    subtotal = db.Column(db.Float())
    total = db.Column(db.Float())
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)
    productoGastoMateria = db.relationship('GastoMateriaPrima', backref='producto', lazy='dynamic')
    productoPedido = db.relationship('Pedido', backref='producto', lazy='dynamic')



class GastoMateriaPrima(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cantidad = db.Column(db.Float())
    costo = db.Column(db.Float())
    materiaPrima_id = db.Column(db.Integer(), db.ForeignKey('materiaprima.id'))
    producto_id = db.Column(db.Integer(), db.ForeignKey('producto.id'))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)


class Pedido(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cantidad = db.Column(db.Float())
    Totalprecio = db.Column(db.Float())
    anticipo = db.Column(db.Float())
    estatusPedido = db.Column(db.String(255))
    fechaCreacion = db.Column(db.DateTime(),default=datetime.datetime.now)
    producto_id = db.Column(db.Integer(), db.ForeignKey('producto.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    pedidoVenta = db.relationship('Venta', backref='pedido', lazy='dynamic')


class Venta(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    deuda = db.Column(db.Float())
    fechaVenta = db.Column(db.DateTime(),default=datetime.datetime.now)
    estatusVenta = db.Column(db.String(255))
    pedido_id = db.Column(db.Integer(), db.ForeignKey('pedido.id'))"""

