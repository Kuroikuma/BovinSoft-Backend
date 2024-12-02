from flask import Blueprint, request, jsonify
from configs.conecction import collections
from controllers.jwt import validar_token
from controllers.premiumRequest_controller import (
    insertar_premium_request,
    mostrar_premium_requests,
    mostrar_todos_premium_requests,
    actualizar_premium_request,
    eliminar_premium_request,
)

premium_request_route = Blueprint('premium_request_routes', __name__)

##validando token
@premium_request_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Historial Sanitario
@premium_request_route.route('/premium_request', methods=['POST'])
def crear_premium_request():
    return insertar_premium_request(collections('premium_request'))

@premium_request_route.route('/premium_request/<id>', methods=['GET'])
def obtener_premium_request_id(id):
    return mostrar_premium_requests(collections('premium_request'), id)

@premium_request_route.route('/premium_request', methods=['GET'])
def obtener_todos_premium_request():
    return mostrar_todos_premium_requests(collections('premium_request'), collections('usuarios'))

@premium_request_route.route('/premium_request/<id>', methods=['PUT'])
def modificar_premium_request_id(id):
    return actualizar_premium_request(collections('premium_request'), id, collections('usuarios'))

@premium_request_route.route('/premium_request/<id>', methods=['DELETE'])
def borrar_premium_request_id(id):
    return eliminar_premium_request(collections('premium_request'), id)
