from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import pymysql

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Conectar SQLAlchemy
    db.init_app(app)

    # Probar conexión a la base de datos
    try:
        with app.app_context():
            connection = pymysql.connect(
                host=app.config['SQLALCHEMY_DATABASE_URI'].split('@')[1].split('/')[0],
                user=app.config['SQLALCHEMY_DATABASE_URI'].split('//')[1].split(':')[0],
                password=app.config['SQLALCHEMY_DATABASE_URI'].split(':')[2].split('@')[0],
                database=app.config['SQLALCHEMY_DATABASE_URI'].split('/')[-1].split('?')[0]
            )
            connection.ping()
            print("Conexión a la base de datos MySQL exitosa.")
            connection.close()
    except Exception as e:
        print(" Error al conectar con la base de datos:")
        print(e)

    # Registrar rutas
    from .routes.device_routes import device_bp
    app.register_blueprint(device_bp)
    return app
