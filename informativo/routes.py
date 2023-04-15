from flask import Blueprint, flash, render_template

from model import Producto


informativo = Blueprint('informativo', __name__)
#Definir la ruta de la pagina informativa sobre nosotros
@informativo.route('/sobre_nosotros', methods=['GET', 'POST'])
def sobre_nosotros():
    return render_template('sobre_nosotros.html')

#Definir la ruta de la pagina informativa contacto
@informativo.route('/contacto', methods=['GET', 'POST'])
def contacto():
    return render_template('contacto.html')

#definir la ruta de la pagina de carrousel

@informativo.route('/carrousel', methods=['GET', 'POST'])
def carrousel():
    productosAll = Producto.query.all()
    return render_template('carrousel.html',informativo=productosAll)

#Definir la ruta para redirigir a la pagina de security.login
@informativo.route('/login', methods=['GET', 'POST'])
def login():
    flash('Por favor, inicie sesión para acceder a esta página')
    return render_template('security/login.html')

#Definir la ruta para la pagina de ver detalle solo informativo del producto
@informativo.route('/ver_detalle/<int:id>', methods=['GET', 'POST'])
def ver_detalle(id):
    producto = Producto.query.get(id)
    return render_template('ver_detalle.html', producto=producto)
