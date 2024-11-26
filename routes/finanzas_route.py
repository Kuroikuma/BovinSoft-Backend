from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.finanza_controller import (
    insertar_finanzas,
    mostrar_finanzas,
    mostrar_todas_finanzas,
    actualizar_finanzas,
    eliminar_finanzas
)

finanzas_route = Blueprint('finanzas_routes', __name__)

##validando token
@finanzas_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Finanzas
@finanzas_route.route('/finanzas', methods=['POST'])
def crear_finanzas():
    return insertar_finanzas(collections('finanzas'))

@finanzas_route.route('/finanzas/<id>', methods=['GET'])
def obtener_finanzas(id):
    return mostrar_finanzas(collections('finanzas'), id)

@finanzas_route.route('/finanzas', methods=['GET'])
def obtener_todas_finanzas():
    return mostrar_todas_finanzas(collections('finanzas'))

@finanzas_route.route('/finanzas/<id>', methods=['PUT'])
def modificar_finanzas(id):
    return actualizar_finanzas(collections('finanzas'), id)

@finanzas_route.route('/finanzas/<id>', methods=['DELETE'])
def borrar_finanzas(id):
    return eliminar_finanzas(collections('finanzas'), id)
