from datetime import datetime
from flask import jsonify, redirect, render_template, request, url_for
from flask import Blueprint, render_template
from flask_security import login_required, current_user
from model import Pedido,db
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
    pedidos = Pedido.query.filter(Pedido.user_id == id).all()
    pedidos_list = []
    for pedido in pedidos:
        pedido_dict = {
            'id': pedido.id,
            'cantidad': pedido.cantidad,
            'precioTotal': pedido.Totalprecio,
            'anticipo': pedido.anticipo,
            'estatusPedido': pedido.estatusPedido,
            # add more attributes as needed
        }
        pedidos_list.append(pedido_dict)
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
        return jsonify({"success":True})