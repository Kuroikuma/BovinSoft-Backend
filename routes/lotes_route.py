from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.lotes_controller import (
    insertar_lote,
    mostrar_lote,
    mostrar_todos_lotes,
    actualizar_lote,
    eliminar_lote
)

lotes_route = Blueprint('lotes_routes', __name__)

##validando token
@lotes_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Lotes
@lotes_route.route('/lotes', methods=['POST'])
def crear_lote():
    return insertar_lote(collections('lotes'))

@lotes_route.route('/lotes/<id>', methods=['GET'])
def obtener_lote(id):
    return mostrar_lote(collections('lotes'), id)

@lotes_route.route('/lotes', methods=['GET'])
def obtener_todos_los_lotes():
    return mostrar_todos_lotes(collections('lotes'))

@lotes_route.route('/lotes/<id>', methods=['PUT'])
def modificar_lote(id):
    return actualizar_lote(collections('lotes'), id)

@lotes_route.route('/lotes/<id>', methods=['DELETE'])
def borrar_lote(id):
    return eliminar_lote(collections('lotes'), id)
