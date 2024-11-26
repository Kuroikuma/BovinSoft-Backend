from flask import Blueprint, request, jsonify
from controllers.jwt import validar_token
from configs.conecction import collections
from controllers.nutricion_controller import (
    insertar_nutricion,
    mostrar_nutricion,
    mostrar_toda_nutricion,
    actualizar_nutricion,
    eliminar_nutricion
)

nutricion_route = Blueprint('nutricion_routes', __name__)

##validando token
@nutricion_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Nutrición
@nutricion_route.route('/nutricion', methods=['POST'])
def crear_nutricion():
    return insertar_nutricion(collections('nutricion'))

@nutricion_route.route('/nutricion/<id>', methods=['GET'])
def obtener_nutricion(id):
    return mostrar_nutricion(collections('nutricion'), id)

@nutricion_route.route('/nutricion', methods=['GET'])
def obtener_toda_la_nutricion():
    return mostrar_toda_nutricion(collections('nutricion'))

@nutricion_route.route('/nutricion/<id>', methods=['PUT'])
def modificar_nutricion(id):
    return actualizar_nutricion(collections('nutricion'), id)

@nutricion_route.route('/nutricion/<id>', methods=['DELETE'])
def borrar_nutricion(id):
    return eliminar_nutricion(collections('nutricion'), id)
