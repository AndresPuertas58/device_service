from ..models.device_model import Device
from sqlalchemy.exc import SQLAlchemyError

def get_devices():
    try:
        print("Consultando lista de dispositivos de red...")
        device = Device.query.all()

        if not device:
            print("No se encontraron dispositivos en la base de datos.")
            return [], 200  #En caso de que la base de datos no tenga registros

        data = [{
            "id": d.id,
            "timestamp": d.timestamp.isoformat(),
            "ip": d.ip,
            "brand": d.brand,
            "hostname": d.hostname,
            "serial_number": d.serial_number,
            "model": d.model,
            "version": d.version,
            "type": d.type
        } for d in device]

        print(f"✅ Se encontraron {len(data)} dispositivos.")
        return data, 200

    except SQLAlchemyError as e:
        print(f" rror de base de datos al consultar dispositivos: {e}")
        return [{"error": "Error de base de datos", "message": "Error en la base de datos" }], 500

    except Exception as e:
        print(f"Error en el servidor al consultar dispositivos: {e}")
        return [{"error": "Error en el servidor", "message": "Error interno del servidor"}], 500

    
