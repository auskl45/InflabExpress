from flask import Blueprint, render_template,flash
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
import logging
from forms import UseForm
from model import Producto,db
from flask import request
from flask import redirect, render_template, url_for

# productos = Blueprint('productos', _name_, url_prefix='/productos')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

productos = Blueprint('productos',__name__)

@productos.route('/profile')
@login_required
#@roles_required('admin','user')
def profile():
    create_forms=UseForm(request.form)
    productosAll=Producto.query.all()
    if current_user.roles[0].name=="admin":
        admin=True
        return render_template('admin/listaProductos.html',form=create_forms,productos=productosAll,admin=admin)

    else:
        admin=False
        return render_template('user/profile.html',name=current_user.name,admin=admin)    

@productos.route('/productosMenu')
@login_required
@roles_required('user')
def productosMenu():
        productosAll=Producto.query.all()
        return render_template('user/productos.html',productos=productosAll)

@productos.route("/agregarProducto",methods=['GET','POST'])
@login_required
@roles_required('admin')
def agregarProducto():
    create_forms=UseForm(request.form)
    if request.method=='POST':
        try:
            product= Producto(nombreProducto=create_forms.nombreProducto.data,
                        precio=create_forms.precio.data,
                        marca=create_forms.marca.data,
                        cantidad=create_forms.cantidad.data)
            db.session.add(product)
            db.session.commit()
            logger.info('Producto agregado por'+current_user.name+' con id '+str(current_user.id))
            return redirect(url_for('productos.profile'))
        except Exception as e:  
            logger.error(str(e) + ' Error al agregar producto por '+current_user.name+' con id '+str(current_user.id))
            flash('Error al agregar producto')
    return render_template('admin/agregar.html',form=create_forms)


@productos.route("/modificarProducto",methods=['GET','POST'])
@login_required
@roles_required('admin')
def modificarProducto():
    create_forms=UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        product= db.session.query(Producto).filter(Producto.id==id).first()
        create_forms.id.data=product.id
        create_forms.nombreProducto.data= product.nombreProducto
        create_forms.precio.data= product.precio
        create_forms.marca.data= product.marca
        create_forms.cantidad.data= product.cantidad


    if request.method=='POST':
        try:
            id=create_forms.id.data
            product= db.session.query(Producto).filter(Producto.id==id).first()
            product.id=create_forms.id.data
            product.nombreProducto=create_forms.nombreProducto.data
            product.precio=create_forms.precio.data
            product.marca=create_forms.marca.data
            product.cantidad=create_forms.cantidad.data

            db.session.add(product)
            db.session.commit()
            logger.info('Producto modificado por '+current_user.name+' con id '+str(current_user.id))
            return redirect(url_for('productos.profile'))
        except Exception as e:    
            logger.error(e)

    return render_template('admin/modificar.html',form=create_forms)

@productos.route("/eliminarProducto")
@login_required
@roles_required('admin')
def eliminarProducto():
        id=request.args.get('id')
        product= db.session.query(Producto).filter(Producto.id==id).first()
        db.session.delete(product)
        db.session.commit()
        logger.info('Producto eliminado por '+current_user.name+' con id '+str(current_user.id))

        # flash("Se ha eliminado el producto")
        return redirect(url_for('productos.profile'))