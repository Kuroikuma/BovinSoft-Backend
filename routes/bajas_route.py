from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.bajas_controller import (
    insertar_baja,
    mostrar_bajas
)

# Inicializando rutas
bajas_route = Blueprint('bajas_routes', __name__)

# validando token
@bajas_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje": "Error de autenticacion, no esta autorizado"})

# ruta crear bajas
@bajas_route.route('/bajas', methods=['POST'])
def insertar_tratamiento_route():
    return insertar_baja(collections('bajas'))

# ruta mostrar bajas
@bajas_route.route('/bajas/',methods=["GET"])
def obtener_reproduccion_id_route(id):
    return mostrar_bajas(collections('bajas'), id)