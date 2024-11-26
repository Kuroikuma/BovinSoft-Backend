from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.bajas_controller import (
    insertar_baja,
    mostrar_bajas,
    mostrar_todas_bajas,
    actualizar_baja,
    eliminar_baja
)

bajas_route = Blueprint('bajas_routes', __name__)

##validando token
@bajas_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})


# Rutas para Bajas
@bajas_route.route('/bajas', methods=['POST'])
def crear_baja():
    return insertar_baja(collections('bajas'))

@bajas_route.route('/bajas/<id>', methods=['GET'])
def obtener_baja(id):
    return mostrar_bajas(collections('bajas'), id)

@bajas_route.route('/bajas', methods=['GET'])
def obtener_todas_bajas():
    return mostrar_todas_bajas(collections('bajas'))

@bajas_route.route('/bajas/<id>', methods=['PUT'])
def modificar_baja(id):
    return actualizar_baja(collections('bajas'), id)

@bajas_route.route('/bajas/<id>', methods=['DELETE'])
def borrar_baja(id):
    return eliminar_baja(collections('bajas'), id)
