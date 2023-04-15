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
from model import MateriaPrima,db
from flask import current_app

from flask import current_app as app
#Definimos la ruta a la página principal


@materiaPrima.route('/profileMateriaPrima')
@login_required
def profileMateriaPrima():
    create_forms=MateriaPrimaForm(request.form)
    materiaPrimaAll=MateriaPrima.query.all()
    if current_user.roles[0].name=="admin":
        admin=True
        return render_template('admin/lista_materia_prima.html',form=create_forms,materiaPrimas=materiaPrimaAll,admin=admin)

    else:
        admin=False
        return render_template('user/profile.html',name=current_user.name,admin=admin)


@materiaPrima.route('/agregar_materia_prima', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def agregar_materia_prima():
    form = MateriaPrimaForm(request.form)
    if request.method == 'POST' and form.validate():
        
        if not form.id_tipo.data:
            flash('Falta el campo id_tipo')
            app.logger.error('Falta llenar el campo id_tipo')
            return redirect(url_for('materiaPrima.agregar_materia_prima'))

        if not form.nombreMateriaPrima.data:
            flash('Falta el campo nombre')
            app.logger.error('Falta llenar el campo nombre')
            return redirect(url_for('materiaPrima.agregar_materia_prima'))
        if not form.color.data:
            flash('Falta el campo color')
            app.logger.error('Falta llenar el campo color')
            return redirect(url_for('materiaPrima.agregar_materia_prima'))
        if not form.costo.data:
            flash('Falta el campo costo')
            app.logger.error('Falta llenar el campo costo')
            return redirect(url_for('materiaPrima.agregar_materia_prima'))
        if not form.stock.data:
            flash('Falta el campo stock')
            app.logger.error('Falta llenar el campo stock')
            return redirect(url_for('materiaPrima.agregar_materia_prima'))
        if not form.idProveedor.data:
            flash('Falta el campo idProveedor')
            app.logger.error('Falta llenar el campo idProveedor')
            return redirect(url_for('materiaPrima.agregar_materia_prima'))
       
        materia_prima = MateriaPrima(id_tipo=form.id_tipo.data, nombreMateriaPrima=form.nombreMateriaPrima.data,
                            color=form.color.data, costo=form.costo.data, stock=form.stock.data, idProveedor=form.idProveedor.data)

        
        db.session.add(materia_prima)
        db.session.commit()
        flash('Materia Prima agregado exitosamente')
        app.logger.info ('Materia Prima agregado exitosamente')
        return redirect(url_for('materiaPrima.profileMateriaPrima'))

    return render_template('admin/agregar_materia_prima.html', form=form)






@materiaPrima.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def editarMateriaPrima(id):
    materiaPrima = MateriaPrima.query.get_or_404(id)
    form = MateriaPrimaForm(request.form, obj=materiaPrima)
    if request.method == 'POST' and form.validate():
        form.populate_obj(materiaPrima)
        db.session.commit()
        return redirect(url_for('materiaPrima.profileMateriaPrima'))

    return render_template('admin/editar_materiaPrima.html', form=form, materiaPrima=materiaPrima)







@materiaPrima.route('/materiaPrima/<int:id>/eliminar', methods=['POST', 'DELETE'])
@login_required
@roles_required('admin')
def eliminar_materiaPrima(id):
    materiaPrima = MateriaPrima.query.get(id)
    if materiaPrima:
        db.session.delete(materiaPrima)
        db.session.commit()
        flash('Materia Prima eliminado exitosamente', 'success')
    else:
        flash('Materia Prima no encontrado', 'error')
    return redirect(url_for('materiaPrima.profileMateriaPrima'))