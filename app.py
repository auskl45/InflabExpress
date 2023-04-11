from flask import Flask, render_template
from Auth.routes import auth
from Pedidos.routes import pedidos
from Productos.routes import productos
from flask_security import current_user,Security, SQLAlchemyUserDatastore
import os
from model import User, Role,db
from config import DevelopmentConfig
userDataStore = SQLAlchemyUserDatastore(db, User, Role)

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
#Definimos la ruta a la página principal
@productos.route('/')
def index():
    return render_template('index.html',current_user=current_user)
@auth.route('/login')
def login():
    return render_template('/security/login.html',current_user=current_user)
@auth.route('/register')
def register():
    return render_template('/security/register.html',current_user=current_user)


app.register_blueprint(auth)
app.register_blueprint(productos)
app.register_blueprint(pedidos)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #     #Generamos la clave aleatoria de sesión Flask para crear una cookie con la inf. de la sesión
app.config['SECRET_KEY'] = os.urandom(24)
# #     # We're using PBKDF2 with salt.
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
#     #Semilla para el método de encriptado que utiliza flask-security
app.config['SECURITY_PASSWORD_SALT'] = 'thisissecretsalt'
security = Security(app, userDataStore)




if __name__=='__main__':
    # csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)