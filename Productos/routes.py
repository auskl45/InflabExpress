from flask import Blueprint, render_template,flash
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
import logging
from forms import UseForm,ProductoForm
from model import Producto,db
from flask import request
from flask import redirect, render_template, url_for
import base64

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
def agregarProducto():
    create_forms=ProductoForm(request.form)
    if request.method=='POST':
        try:
            imagenR= request.files['image']
            imagen = base64.b64encode(imagenR.read())
            product= Producto(
                 nombre = create_forms.nombre.data,
                 descripcion = create_forms.descripcion.data,
                 stock = create_forms.stock.data,
                 altura = create_forms.altura.data,
                 ancho = create_forms.ancho.data,
                 largo = create_forms.largo.data,
                 image = imagen,
                 subtotal = create_forms.subtotal.data,
                 total = create_forms.total.data)
            db.session.add(product)
            db.session.commit()
            logger.info('Producto agregado por'+current_user.name+' con id '+str(current_user.id))
            return redirect(url_for('productos.profile'))
        except Exception as e:  
            logger.error(str(e) + ' Error al agregar producto por '+current_user.name+' con id '+str(current_user.id))
            flash('Error al agregar producto')
    return render_template('admin/agregar.html',form=create_forms)


@productos.route("/modificarProducto",methods=['GET','POST'])
def modificarProducto():
    create_forms=ProductoForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        product= db.session.query(Producto).filter(Producto.id==id).first()
        create_forms.id.data=product.id
        create_forms.nombre.data= product.nombre
        create_forms.descripcion.data= product.descripcion
        create_forms.stock.data= product.stock
        create_forms.altura.data= product.altura
        create_forms.ancho.data= product.ancho
        create_forms.largo.data= product.largo
        create_forms.subtotal.data= product.subtotal
        create_forms.total.data= product.total
        create_forms.image.data= product.image
        """create_forms.id.data=product.id
        create_forms.nombreProducto.data= product.nombreProducto
        create_forms.precio.data= product.precio
        create_forms.marca.data= product.marca
        create_forms.cantidad.data= product.cantidad"""


    if request.method=='POST':
        try:
            imagenR= request.files['imageM']
            imagen = base64.b64encode(imagenR.read())
            #print(len(str(imagen)))
            if len(str(imagen)) < 4:
                id=create_forms.id.data
                product= db.session.query(Producto).filter(Producto.id==id).first()
                product.id=create_forms.id.data
                product.nombre=create_forms.nombre.data
                product.descripcion=create_forms.descripcion.data
                product.stock=create_forms.stock.data
                product.altura=create_forms.altura.data
                product.ancho=create_forms.ancho.data
                product.largo=create_forms.largo.data
                product.subtotal=create_forms.subtotal.data
                product.total=create_forms.total.data
                db.session.add(product)
                db.session.commit()
                logger.info('Producto modificado por '+current_user.name+' con id '+str(current_user.id))
                return redirect(url_for('productos.profile'))
            else:
                id=create_forms.id.data
                product= db.session.query(Producto).filter(Producto.id==id).first()
                product.id=create_forms.id.data
                product.nombre=create_forms.nombre.data
                product.descripcion=create_forms.descripcion.data
                product.stock=create_forms.stock.data
                product.altura=create_forms.altura.data
                product.ancho=create_forms.ancho.data
                product.largo=create_forms.largo.data
                product.subtotal=create_forms.subtotal.data
                product.total=create_forms.total.data
                product.image=imagen
                db.session.add(product)
                db.session.commit()
                logger.info('Producto modificado por '+current_user.name+' con id '+str(current_user.id))
                return redirect(url_for('productos.profile'))
        except Exception as e:    
            logger.error(e)

    return render_template('admin/modificar.html',form=create_forms)

@productos.route("/eliminarProducto")
def eliminarProducto():
        id=request.args.get('id')
        product= db.session.query(Producto).filter(Producto.id==id).first()
        db.session.delete(product)
        db.session.commit()
        logger.info('Producto eliminado por '+current_user.name+' con id '+str(current_user.id))

        # flash("Se ha eliminado el producto")
        return redirect(url_for('productos.profile'))