from flask import Blueprint, request, jsonify
from configs.conecction import collections
from controllers.jwt import validar_token
from controllers.calendario_cuidados_controller import (
    insertar_calendario_cuidado,
    mostrar_calendario_cuidados,
    mostrar_todos_calendario_cuidados,
    actualizar_calendario_cuidado,
    eliminar_calendario_cuidado,
    mostrar_calendario_cuidado_por_bovino_id,
    mostrar_calendario_cuidado_por_finca_id
)

calendario_cuidado_route = Blueprint('calendario_cuidado_routes', __name__)

##validando token
@calendario_cuidado_route.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Mensaje":"Error de autenticacion, no estas autorizado"})

# Rutas para Historial Sanitario
@calendario_cuidado_route.route('/calendario_cuidado', methods=['POST'])
def crear_calendario_cuidado():
    return insertar_calendario_cuidado(collections('calendario_cuidado'))

@calendario_cuidado_route.route('/calendario_cuidado/<id>', methods=['GET'])
def obtener_calendario_cuidado(id):
    return mostrar_calendario_cuidados(collections('calendario_cuidado'), id)

@calendario_cuidado_route.route('/calendario_cuidado', methods=['GET'])
def obtener_todos_calendario_cuidados():
    return mostrar_todos_calendario_cuidados(collections('calendario_cuidado'))

@calendario_cuidado_route.route('/calendario_cuidado/<id>', methods=['PUT'])
def modificar_calendario_cuidado(id):
    return actualizar_calendario_cuidado(collections('calendario_cuidado'), id)

@calendario_cuidado_route.route('/calendario_cuidado/<id>', methods=['DELETE'])
def borrar_calendario_cuidado(id):
    return eliminar_calendario_cuidado(collections('calendario_cuidado'), id)

@calendario_cuidado_route.route('/calendario_cuidado/bovino/<bovino_id>', methods=['GET'])
def obtener_calendario_cuidado_por_bovino_id(bovino_id):
    return mostrar_calendario_cuidado_por_bovino_id(collections('calendario_cuidado'), collections('bovinos'), bovino_id)
  
@calendario_cuidado_route.route('/calendario_cuidado/finca/<finca_id>', methods=['GET'])
def obtener_calendario_cuidado_por_finca_id(finca_id):
    return mostrar_calendario_cuidado_por_finca_id(collections('calendario_cuidado'), collections('bovinos'), finca_id)
