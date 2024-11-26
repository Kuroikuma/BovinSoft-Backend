from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.reproduccion_controller import (
    insertar_reproduccion,
    obtener_reproduccion,
    actualizar_reproduccion,
    eliminar_reproduccion
)

# Inicializando rutas
reproduccion_route = Blueprint('reproduccion_routes', __name__)

# validando token
@reproduccion_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje": "Error de autenticacion, no esta autorizado"})

# ruta crear reproduccion
@reproduccion_route.route('/reproduccion', methods=['POST'])
def insertar_reproduccion_route():
    return insertar_reproduccion(collections('reproduccion'))

# ruta mostrar por id
@reproduccion_route.route('/reprduccion/<id>',methods=["GET"])
def obtener_reproduccion_id_route(id):
    return obtener_reproduccion(collections('reproduccion'), id)

# ruta actualizar por id
@reproduccion_route.route('/reproduccion/<id>', methods=['PUT'])
def actualizar_reproduccion_id_route(id):
    return actualizar_reproduccion(collections('reproduccion', id))

# ruta eliminar por id
@reproduccion_route.route('/reproduccion/<id>', methods=['DELETE'])
def eliminar_reproduccion_id_route(id):
    return eliminar_reproduccion(collections('reproduccion'), id)