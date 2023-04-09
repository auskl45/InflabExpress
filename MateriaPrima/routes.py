from flask import Blueprint, render_template,flash
materiaPrima = Blueprint('materiaPrima', __name__)

from flask_security import login_required, current_user
#Importamos la clase Blueprint del módulo flask
from flask import Blueprint, flash, redirect, render_template, request, url_for
#Importamos login_required, current_user de flask_security
from flask_security import login_required, current_user, roles_accepted
#Importamos el decorador login_required de flask_security
from flask_security.decorators import roles_required
from forms import MateriaPrimaForm, UseForm
#Importamos el objeto de la BD desde __init__.py
from model import Producto
from model import MateriaPrima,db, TipoMateriaPrima, Proveedor
from flask import current_app

from flask import current_app as app
#Definimos la ruta a la página principal


@materiaPrima.route('/profileMateriaPrima')
@login_required
def profileMateriaPrima():
    create_forms=MateriaPrimaForm(request.form)
    tipoMateriaPrimaAll= TipoMateriaPrima.query.all()
    proveedorAll=Proveedor.query.all()
    materiaPrimaAll=MateriaPrima.query.all()
    if current_user.roles[0].name=="admin":
        admin=True
        return render_template('admin/listaMateriaPrima.html',form=create_forms,materiaPrimas=materiaPrimaAll,tipoMateriaPrima=tipoMateriaPrimaAll,proveedor=proveedorAll,admin=admin)

    else:
        admin=False
        return render_template('user/profile.html',name=current_user.name,admin=admin)


@materiaPrima.route('/agregar_materia_prima', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def agregar_materia_prima():
    form = MateriaPrimaForm(request.form)
    tipoMateriaPrimaAll = TipoMateriaPrima.query.all()
    proveedorAll = Proveedor.query.all()
    if request.method == 'POST' and form.validate():

        materia_prima = MateriaPrima(
            nombre=form.nombre.data,
            color=form.color.data,
            costo=form.costo.data,
            stock=form.stock.data,
            tipoMateriaPrima_id=request.form['tipoMateriaPrima_id'],
            proveedor_id=request.form['proveedor_id'])
        db.session.add(materia_prima)
        db.session.commit()
        flash('Materia Prima agregado exitosamente')
        app.logger.info ('Materia Prima agregado exitosamente')
        return redirect(url_for('materiaPrima.profileMateriaPrima'))

    return render_template('admin/agregarMateriaPrima.html', form=form, tipoMateriaPrima=tipoMateriaPrimaAll, proveedores=proveedorAll)




@materiaPrima.route('/modificarMateriaPrima', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def modificarMateriaPrima():
    form = MateriaPrimaForm(request.form)
    tipoMateriaPrimaAll = TipoMateriaPrima.query.all()
    proveedorAll = Proveedor.query.all()
    if request.method == 'GET':
        id = request.args.get('id')
        materiaPrima = db.session.query(MateriaPrima).filter(MateriaPrima.id == id).first()
        form.id.data = materiaPrima.id
        form.nombre.data = materiaPrima.nombre
        form.color.data = materiaPrima.color
        form.costo.data = materiaPrima.costo
        form.stock.data = materiaPrima.stock
        form.tipoMateriaPrima_id.data = materiaPrima.tipoMateriaPrima_id
        form.proveedor_id.data = materiaPrima.proveedor_id

    if request.method == 'POST' and form.validate():
        id = form.id.data
        materiaPrima = db.session.query(MateriaPrima).filter(MateriaPrima.id == id).first()
        materiaPrima.nombre = form.nombre.data
        materiaPrima.color = form.color.data
        materiaPrima.costo = form.costo.data
        materiaPrima.stock = form.stock.data
        materiaPrima.tipoMateriaPrima_id = request.form['tipoMateriaPrima_id']
        materiaPrima.proveedor_id = request.form['proveedor_id']
        db.session.add(materiaPrima)
        db.session.commit()
        flash('Materia Prima modificado exitosamente', 'success')
        return redirect(url_for('materiaPrima.profileMateriaPrima'))

    return render_template('admin/editarMateriaPrima.html', form=form, tipoMateriaPrima=tipoMateriaPrimaAll, proveedores=proveedorAll)


@materiaPrima.route('/eliminarMateriaPrima')
@login_required
@roles_required('admin')
def eliminarMateriaPrima():
    id = request.args.get('id')
    materiaPrima = db.session.query(MateriaPrima).filter(MateriaPrima.id == id).first()
    db.session.delete(materiaPrima)
    db.session.commit()
    #flash('Materia Prima eliminado exitosamente', 'success')

    return redirect(url_for('materiaPrima.profileMateriaPrima'))

@materiaPrima.route('/agregarTipoMateria', methods=['POST'])
@login_required
def agregarTipoMateria():
    if request.method == 'POST':
        tipoMateriaPrima = TipoMateriaPrima(
            tipo = request.form['tipoMateriaPrimaNombre'],
            UnidadMedida = request.form['UnidadMedidaMateria']
        )
        db.session.add(tipoMateriaPrima)
        db.session.commit()
        flash('Tipo Materia Prima agregado exitosamente')
        return redirect(url_for('materiaPrima.agregar_materia_prima'))