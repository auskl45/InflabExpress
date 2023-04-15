from flask import Blueprint, render_template,flash
proveedor = Blueprint('proveedor', __name__)
from flask_security import login_required, current_user
#Importamos la clase Blueprint del módulo flask
from flask import Blueprint, flash, redirect, render_template, request, url_for
#Importamos login_required, current_user de flask_security
from flask_security import login_required, current_user, roles_accepted
#Importamos el decorador login_required de flask_security
from flask_security.decorators import roles_required
from forms import ProveedorForm
#Importamos el objeto de la BD desde __init__.py
from model import Proveedor,db
from flask import current_app

from flask import current_app as app
#Definimos la ruta a la página principal

@proveedor.route('/profileProveedor')
@login_required
def profileProveedor():
    create_forms=ProveedorForm(request.form)
    proveedorAll=Proveedor.query.all()
    if current_user.roles[0].name=="admin":
        admin=True
        return render_template('admin/lista_proveedor.html',form=create_forms,proveedores=proveedorAll,admin=admin)

    else:
        admin=False
        return render_template('user/profile.html',name=current_user.name,admin=admin)
    
@proveedor.route('/agregar_proveedor', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def agregar_proveedor():
    form = ProveedorForm(request.form)
    if request.method == 'POST' and form.validate():
        
        if not form.nombre.data:
            flash('Falta el campo nombre')
            app.logger.error('Falta llenar el campo nombre')
            return redirect(url_for('proveedor.agregar_proveedor'))
        if not form.direccion.data:
            flash('Falta el campo direccion')
            app.logger.error('Falta llenar el campo direccion')
            return redirect(url_for('proveedor.agregar_proveedor'))
        if not form.telefono.data:
            flash('Falta el campo telefono')
            app.logger.error('Falta llenar el campo telefono')
            return redirect(url_for('proveedor.agregar_proveedor'))
        if not form.email.data:
            flash('Falta el campo email')
            app.logger.error('Falta llenar el campo email')
            return redirect(url_for('proveedor.agregar_proveedor'))
        
        proveedor=Proveedor(nombre=form.nombre.data,direccion=form.direccion.data,telefono=form.telefono.data,email=form.email.data)
        db.session.add(proveedor)
        db.session.commit()
        flash('Proveedor creado correctamente')
        app.logger.info('Proveedor creado correctamente')
        return redirect(url_for('proveedor.profileProveedor'))
    return render_template('admin/agregar_proveedor.html', form=form)

@proveedor.route('/editarProveedor/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def editarProveedor(id):
    proveedor=Proveedor.query.get_or_404(id)
    form=ProveedorForm(request.form,obj=proveedor)
    if request.method == 'POST' and form.validate():
        form.populate_obj(proveedor)
        db.session.commit()
        flash('Proveedor actualizado correctamente')
        app.logger.info('Proveedor actualizado correctamente')
        return redirect(url_for('proveedor.profileProveedor'))
    return render_template('admin/editar_proveedor.html', form=form,proveedor=proveedor)

@proveedor.route('/proveedor/<int:id>/eliminar', methods=['POST', 'DELETE'])
@login_required
@roles_required('admin')
def eliminar_proveedor(id):
    proveedor=Proveedor.query.get(id)
    if proveedor:
        db.session.delete(proveedor)
        db.session.commit()
        flash('Proveedor eliminado correctamente')
        app.logger.info('Proveedor eliminado correctamente')
    else:
        flash('Proveedor no encontrado','error')
        app.logger.error('Proveedor no encontrado')
    return redirect(url_for('proveedor.profileProveedor'))