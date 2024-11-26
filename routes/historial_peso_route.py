from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.historialpeso_controller import (
    insertar_historial_peso,
    mostrar_historial_peso,
    mostrar_todos_historiales_peso,
    actualizar_historial_peso,
    eliminar_historial_peso
)

historial_peso_route = Blueprint('historial_peso_routes', __name__)

##validando token
@historial_peso_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Historial de Peso
@historial_peso_route.route('/historial_peso', methods=['POST'])
def crear_historial_peso():
    return insertar_historial_peso(collections('historial_peso'))

@historial_peso_route.route('/historial_peso/<id>', methods=['GET'])
def obtener_historial_peso(id):
    return mostrar_historial_peso(collections('historial_peso'), id)

@historial_peso_route.route('/historial_peso', methods=['GET'])
def obtener_todos_historiales_peso():
    return mostrar_todos_historiales_peso(collections('historial_peso'))

@historial_peso_route.route('/historial_peso/<id>', methods=['PUT'])
def modificar_historial_peso(id):
    return actualizar_historial_peso(collections('historial_peso'), id)

@historial_peso_route.route('/historial_peso/<id>', methods=['DELETE'])
def borrar_historial_peso(id):
    return eliminar_historial_peso(collections('historial_peso'), id)
