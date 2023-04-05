from flask import Blueprint, render_template, redirect, url_for, request, flash,current_app
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from flask_security import login_required
from flask_security import SQLAlchemyUserDatastore
#########################################################################################
from flask_security.utils import login_user, logout_user, hash_password, encrypt_password
##########################################################################################
from model import User,Role,db
userDataStore = SQLAlchemyUserDatastore(db, User, Role)



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#Creamos el BluePrint y establecemos que todas estas rutas deben estar dentro de /security para sobre escribir las vistas por omisión de flask-security.
#Por lo que ahora las rutas deberán ser /security/login y security/register
auth = Blueprint('auth', __name__, url_prefix='/security')



@auth.route('/login', methods=['POST'])
def login_post():

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()

    if len(email)==0 or len(password)==0:
        flash('Rellene los campos')
        logger.warning('Error campos vacios')

        return redirect(url_for('auth.login'))

    #Verificamos si el usuario existe
    #Tomamos el password proporcionado por el usuario lo hasheamos, y lo comparamos con el password de la base de datos.
    if not user or not check_password_hash(user.password, password):
    #if not user or not user.password==encrypt_password(password):
        #Si el usuario no existe o no coinciden los passwords
        flash('El usuario y/o la contraseña son incorrectos')
        # current_app.logger.error('El usuario y/o la contraseña son incorrectos')
        logger.warning('El usuario y/o la contraseña son incorrectos')
        print('El correo electrónico es incorrecto')


        return redirect(url_for('auth.login')) #Si el usuario no existe o el password es incorrecto regresamos a login
    
    #Si llegamos a este punto sabemos que el usuario tiene datos correctos.
    #Creamos una sessión y logueamos al usuario
    login_user(user, remember=remember)
    # logger.info('email: ' + email +' name: ' + user.name+' idUser: ' + str(user.id))
    return redirect(url_for('productos.profile'))


@auth.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    #Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()
 
    if user: #Si se encontró un usuario, redireccionamos de regreso a la página de registro
        flash('El correo electrónico ya existe')
        # current_app.logger.error('El correo electrónico ya existe')
        logger.warning('El correo electrónico ya existe')

        return redirect(url_for('auth.register'))

    #Creamos un nuevo usuario con los datos del formulario.
    # Hacemos un hash a la contraseña para que no se guarde la versión de texto sin formato
    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    userDataStore.create_user(
        name=name, email=email, password=generate_password_hash(password, method='sha256')
    )

    # db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    #Cerramos la sessión
    logout_user()
    return redirect(url_for('productos.index'))
