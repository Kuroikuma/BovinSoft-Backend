from flask import Blueprint, request, jsonify
from configs.conecction import collections
from controllers.jwt import validar_token
from controllers.historial_sanitario_controller import (
    insertar_historial_sanitario,
    mostrar_historial_sanitario,
    mostrar_todos_historiales_sanitarios,
    actualizar_historial_sanitario,
    eliminar_historial_sanitario
)

historial_sanitario_route = Blueprint('historial_sanitario_routes', __name__)

##validando token
@historial_sanitario_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Historial Sanitario
@historial_sanitario_route.route('/historial_sanitario', methods=['POST'])
def crear_historial_sanitario():
    return insertar_historial_sanitario(collections('historial_sanitario'))

@historial_sanitario_route.route('/historial_sanitario/<id>', methods=['GET'])
def obtener_historial_sanitario(id):
    return mostrar_historial_sanitario(collections('historial_sanitario'), id)

@historial_sanitario_route.route('/historial_sanitario', methods=['GET'])
def obtener_todos_historiales_sanitarios():
    return mostrar_todos_historiales_sanitarios(collections('historial_sanitario'))

@historial_sanitario_route.route('/historial_sanitario/<id>', methods=['PUT'])
def modificar_historial_sanitario(id):
    return actualizar_historial_sanitario(collections('historial_sanitario'), id)

@historial_sanitario_route.route('/historial_sanitario/<id>', methods=['DELETE'])
def borrar_historial_sanitario(id):
    return eliminar_historial_sanitario(collections('historial_sanitario'), id)
