from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.propietario_controller import (
    insertar_propietario,
    mostrar_propietario,
    mostrar_todos_propietarios,
    actualizar_propietario,
    eliminar_propietario
)

propietario_route = Blueprint('propietario_routes', __name__)

##validando token
@propietario_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Propietarios
@propietario_route.route('/propietarios', methods=['POST'])
def crear_propietario():
    return insertar_propietario(collections('propietarios'))

@propietario_route.route('/propietarios/<id>', methods=['GET'])
def obtener_propietario(id):
    return mostrar_propietario(collections('propietarios'), id)

@propietario_route.route('/propietarios', methods=['GET'])
def obtener_todos_propietarios():
    return mostrar_todos_propietarios(collections('propietarios'))

@propietario_route.route('/propietarios/<id>', methods=['PUT'])
def modificar_propietario(id):
    return actualizar_propietario(collections('propietarios'), id)

@propietario_route.route('/propietarios/<id>', methods=['DELETE'])
def borrar_propietario(id):
    return eliminar_propietario(collections('propietarios'), id)
