from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
# import forms

from flask import jsonify
# Se genera la configuracion de la base de datos
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from model import db
from model import Pedido
from db import get_connection
import forms


pedidos = Blueprint('pedidos', __name__)


@pedidos.route('/getPedidos', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def getPedidos():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "call getpedidos()"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            admin=True
    except Exception as e:
        print("Error: ", e)
        pass

    return render_template('admin/getPedidos.html', pedidos=resultset,admin=admin)


@pedidos.route('/realizarInflable', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def realizarInflable():
    # if request.method == 'GET':
    idPedido = request.args.get('id')
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call cambiarEstatusInflable(%s, %s)',(idPedido, 3,))
            connection.commit()
            connection.close()
    except Exception as e:
        print("Error 1: ", e)
        pass
    return redirect(url_for('pedidos.getPedidos'))

@pedidos.route('/cancelarPedido', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def cancelarInflable():
    # if request.method == 'GET':
    idInflable = request.args.get('id')
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call cambiarEstatusInflable(%s, %s)',(idInflable, 0,))
            connection.commit()
            connection.close()
            
    except Exception as e:
        print("Error 1: ", e)
        pass
    return redirect(url_for('pedidos.getPedidos'))

@pedidos.route('/procesarPedido', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def procesarPedido():
    # if request.method == 'GET':
    idInflable = request.args.get('id')
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call cambiarEstatusInflable(%s, %s)',(idInflable, 2,))
            connection.commit()
            connection.close()
    except Exception as e:
        print("Error 1: ", e)
        pass
    return redirect(url_for('pedidos.getPedidos'))

