from flask import Blueprint, render_template,flash
gastoMateriaPrima = Blueprint('gastoMateriaPrima', __name__)

from flask_security import login_required, current_user
#Importamos la clase Blueprint del módulo flask
from flask import Blueprint, flash, redirect, render_template, request, url_for
#Importamos login_required, current_user de flask_security
from flask_security import login_required, current_user, roles_accepted
#Importamos el decorador login_required de flask_security
from flask_security.decorators import roles_required
from forms import GastoMateriaPrimaForm, UseForm
#Importamos el objeto de la BD desde __init__.py
from model import Producto
from model import MateriaPrima,db, GastoMateriaPrima
from flask import current_app

from flask import current_app as app
#Definimos la ruta a la página principal


@gastoMateriaPrima.route('/profileGastoMateriaPrima')
@login_required
def profileGastoMateriaPrima():
    create_forms=GastoMateriaPrimaForm(request.form)
    gastomateriaPrimaAll= GastoMateriaPrima.query.all()
    inflablesAll= Producto.query.all()
    materiaPrimaAll= MateriaPrima.query.all()
    if current_user.roles[0].name=="admin":
        admin=True
        return render_template('admin/listaGastoMateriaPrima.html',form=create_forms,materiaPrimas=materiaPrimaAll,admin=admin,gastomateriaPrima=gastomateriaPrimaAll,inflables=inflablesAll)
    else:
        admin=False
        return render_template('user/profile.html',name=current_user.name,admin=admin)


@gastoMateriaPrima.route('/agregarGastoMateria', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def agregarGastoMateria():
    form = GastoMateriaPrimaForm(request.form)
    inflablesAll= Producto.query.all()
    materiaPrimaAll= MateriaPrima.query.all()
    if request.method == 'POST' and form.validate():

        gasto_materia_prima = GastoMateriaPrima(
            cantidad=request.form['cantidadGastada'],
            costo=form.total.data,
            producto_id=request.form['inflable_id'],
            materiaPrima_id=request.form['materiaPrima_id'])
        db.session.add(gasto_materia_prima)
        db.session.commit()
        flash('Gasto Materia Prima agregado exitosamente')
        app.logger.info ('Gasto Materia Prima agregado exitosamente')
        return redirect(url_for('gastoMateriaPrima.profileGastoMateriaPrima'))
    return render_template('admin/agregarGastoMateriaPrima.html', form=form, inflables=inflablesAll, materiaPrimas=materiaPrimaAll)



@gastoMateriaPrima.route('/modificarGastoMateria', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def modificarGastoMateria():
    form = GastoMateriaPrimaForm(request.form)
    inflablesAll= Producto.query.all()
    materiaPrimaAll= MateriaPrima.query.all()
    if request.method == 'GET':
        id = request.args.get('id')
        gastoMateriaPrima = db.session.query(GastoMateriaPrima).filter(GastoMateriaPrima.id == id).first()
        form.id.data = gastoMateriaPrima.id
        form.cantidad.data = gastoMateriaPrima.cantidad
        form.total.data = gastoMateriaPrima.costo
        form.producto_id.data = int(gastoMateriaPrima.producto_id)
        form.materiaPrima_id.data = int(gastoMateriaPrima.materiaPrima_id)
        print(form.id.data)
        print(form.cantidad.data)
        print(form.total.data)
        print(form.producto_id.data)
        print(form.materiaPrima_id.data)

    if request.method == 'POST' and form.validate():
        id = form.id.data
        gastoMateriaPrima = db.session.query(GastoMateriaPrima).filter(GastoMateriaPrima.id == id).first()
        gastoMateriaPrima.cantidad = form.cantidad.data
        gastoMateriaPrima.costo = form.total.data
        gastoMateriaPrima.producto_id = request.form['inflable_id']
        gastoMateriaPrima.materiaPrima_id = request.form['materiaPrima_id']
        db.session.add(gastoMateriaPrima)
        db.session.commit()
        flash('Gasto Materia Prima modificado exitosamente', 'success')
        return redirect(url_for('gastoMateriaPrima.profileGastoMateriaPrima'))

    return render_template('admin/editarGastoMateriaPrima.html', form=form, inflables=inflablesAll, materiaPrimas=materiaPrimaAll)
    

@gastoMateriaPrima.route('/eliminarGastoMateria', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def eliminarGastoMateria():
    id = request.args.get('id')
    gastoMateriaPrima = db.session.query(GastoMateriaPrima).filter(GastoMateriaPrima.id == id).first()
    db.session.delete(gastoMateriaPrima)
    db.session.commit()
    #flash('Gasto Materia Prima eliminado exitosamente', 'success')
    return redirect(url_for('gastoMateriaPrima.profileGastoMateriaPrima'))

"""
@gastoMateriaPrima.route('/modificarMateriaPrima', methods=['GET', 'POST'])
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


@gastoMateriaPrima.route('/eliminarMateriaPrima')
@login_required
@roles_required('admin')
def eliminarMateriaPrima():
    id = request.args.get('id')
    materiaPrima = db.session.query(MateriaPrima).filter(MateriaPrima.id == id).first()
    db.session.delete(materiaPrima)
    db.session.commit()
    #flash('Materia Prima eliminado exitosamente', 'success')

    return redirect(url_for('materiaPrima.profileMateriaPrima'))

@gastoMateriaPrima.route('/agregarTipoMateria', methods=['POST'])
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
        return redirect(url_for('materiaPrima.agregar_materia_prima'))"""