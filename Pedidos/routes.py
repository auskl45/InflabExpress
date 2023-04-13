from datetime import datetime
from flask import jsonify, redirect, render_template, request, url_for
from flask import Blueprint, render_template
from flask_security import login_required, current_user
from model import Pedido,Producto,db
from flask_security.decorators import roles_required
pedidos = Blueprint('pedidos',__name__)

@pedidos.route('/pedidosMenu',methods=['GET','POST'])
@login_required
@roles_required('user')
def pedidosMenu():
     return render_template('user/pedidos.html')

@pedidos.route('/mostrarPedidos/<id>', methods=['GET', 'POST'])
@login_required
@roles_required('user')
def mostrarPedidos(id):
    query = db.session.query(Pedido, Producto).join(
        Producto, Pedido.producto_id == Producto.id
    )
    query = query.filter(Pedido.user_id == id)
    # extract specific fields and convert the results to a list of dictionaries
    pedidos = query.all()
    pedidos_list = []
    for pedido, producto in pedidos:
        pedido_dict = {
            'id': pedido.id,
            'fechaPedido': pedido.fechaCreacion,
            'nombreProducto': producto.nombre,
            'altura': producto.altura,
            'ancho': producto.ancho,
            'largo': producto.largo,
            'cantidad': pedido.cantidad,
            'estatusPedido': pedido.estatusPedido,
            'precioUnitario': producto.total,
            'precioTotal': pedido.Totalprecio,
            'anticipo': pedido.anticipo,
            'estatusPedido': pedido.estatusPedido,
            # add more attributes as needed
        }
        pedidos_list.append(pedido_dict)
        # print(pedido.id,producto.id,producto.stock)
    # pedidos = Pedido.query.filter(Pedido.user_id == id).all()
    # pedidos_list = []
    # for pedido in pedidos:
    #     pedido_dict = {
    #         'id': pedido.id,
    #         'cantidad': pedido.cantidad,
    #         'precioTotal': pedido.Totalprecio,
    #         'anticipo': pedido.anticipo,
    #         'estatusPedido': pedido.estatusPedido,
    #         # add more attributes as needed
    #     }
    #     pedidos_list.append(pedido_dict)
    return jsonify(pedidos_list)

@pedidos.route('/realizarPedido',methods=['GET','POST'])
@login_required
@roles_required('user')
def realizarPedido():
        jsdata = request.get_json()
        for data in jsdata:
            
            totalPrecio=data['precio']*data['cantidadAñadido']
            anticipo= totalPrecio*0.50
            pedido= Pedido(cantidad=data['cantidadAñadido'],
                         Totalprecio=totalPrecio,
                         anticipo=anticipo,
                         estatusPedido="activo",
                         fechaCreacion=datetime.now().strftime('%Y-%m-%d %H:%M:%S') ,
                         producto_id=data['idProducto'],
                         user_id=data['idUsuario'])
            db.session.add(pedido)
            db.session.commit()
            stock=int(data['cantidadMaxima'])-data['cantidadAñadido']
            product= db.session.query(Producto).filter(Producto.id==data['idProducto']).first()
            product.stock=stock
            db.session.add(product)
            db.session.commit()
        return jsonify({"success":True})