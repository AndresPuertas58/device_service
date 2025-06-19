from flask import Blueprint, jsonify
from ..services.device_service import get_devices

device_bp = Blueprint('device_bp', __name__, url_prefix="/api")

@device_bp.route("/device_list", methods=["GET"])
def device_list():
    result, status = get_devices()
    return jsonify(result), status
    

