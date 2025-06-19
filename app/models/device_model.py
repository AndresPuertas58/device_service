from .. import db  # <- Asegúrate de importar desde app.__init__.py

class Device(db.Model):
    __tablename__ = 'devices_of_network'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    hostname = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    serial_number = db.Column(db.String(20), nullable=False)
    version = db.Column(db.String(20), nullable=False)
