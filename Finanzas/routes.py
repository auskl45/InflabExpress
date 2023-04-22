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


finanzas = Blueprint('finanzas', __name__)


@finanzas.route('/getfinanzas', methods=['GET', 'POST'])
# @login_required
# @roles_required('admin','user')
def getfinanzas():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "call getFinanzasInformacion()"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            finanzas= list(resultset)
            print(resultset[0])
            print(list(resultset))
            print(finanzas[0][0])
    except Exception as e:
        print("Error: ", e)
        pass

    return render_template('admin/finanzas.html',admin=True, finanzas=finanzas)

