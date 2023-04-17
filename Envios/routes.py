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


envios = Blueprint('envios', __name__)


@envios.route('/getEnvios', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def getEnvios():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "call getEnvios()"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            admin=True
    except Exception as e:
        print("Error: ", e)
        pass

    return render_template('admin/envios.html', envios=resultset,admin=admin,completo=False)


@envios.route('/modificarEnvio', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def modificarEnvio():
    if request.method == 'POST':
        print("entro")
        idEnvio = request.form.get("txtIdEnvio")
        proveedor = request.form.get("txtProveedor")
        noSeguimiento = request.form.get("txtNoSeguimiento")
        fechaEntrega = request.form.get("txtFechaEntrega")
        print(idEnvio)
        print(proveedor)
        print(noSeguimiento)
        print(fechaEntrega)
       
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call modificarEnvios(%s, %s, %s, %s)',(idEnvio, proveedor, fechaEntrega, noSeguimiento,))
                connection.commit()
                connection.close()
        except Exception as e:
            print("Error 1: ", e)
            pass
        return redirect(url_for('envios.getEnvios'))
    
    
@envios.route('/cancelarEnvio', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def cancelarEnvio():
    if request.method == 'GET':
        print("entro")
        idEnvio = request.args.get('id')
        
        print(idEnvio)
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call cambiarEstatusEnvio(%s, %s)',(idEnvio,0,))
                connection.commit()
                connection.close()
        except Exception as e:
            print("Error 1: ", e)
            pass
        return redirect(url_for('envios.getEnvios'))

@envios.route('/completarEnvio', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def completarEnvio():
    if request.method == 'GET':
        idEnvio = request.args.get('id')
        
        print(idEnvio)
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call cambiarEstatusEnvio(%s, %s)',(idEnvio,3,))
                connection.commit()
                connection.close()
        except Exception as e:
            print("Error 1: ", e)
            pass
        return redirect(url_for('envios.getEnvios'))
    
@envios.route('/getEnviosCompletados', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def getEnviosCompletados():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "call getEnviosCompletados()"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            admin=True
    except Exception as e:
        print("Error: ", e)
        pass

    return render_template('admin/envios.html', envios=resultset,admin=admin, completo=True)
