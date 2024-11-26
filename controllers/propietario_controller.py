from flask import request, jsonify
from models.propietario import Propietario
from bson import ObjectId

# Insertar propietario
def insertar_propietario(collection):
    try:
        data = request.get_json()
        propietario = Propietario(
            nombre=data['nombre'],
            contacto=data['contacto'],
            direccion=data['direccion']
        )
        propietario_data = propietario.to_dic()
        collection.insert_one(propietario_data)
        return jsonify({"Mensaje": "Propietario registrado exitosamente", "propietario": propietario_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar propietario por id
def mostrar_propietario(collection, id):
    try:
        propietario = collection.find_one({"_id": ObjectId(id)})
        if propietario:
            return jsonify({"propietario": propietario}), 200
        else:
            return jsonify({"Mensaje": "Propietario no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todos los propietarios
def mostrar_todos_propietarios(collection):
    try:
        registros = collection.find()
        propietarios = []
        for registro in registros:
            registro['_id'] = str(registro['_id'])  # Convertir ObjectId a string
            propietarios.append(registro)
        return jsonify({"propietarios": propietarios}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar propietario
def actualizar_propietario(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'nombre' in data:
            actualizar_datos['nombre'] = data['nombre']
        if 'contacto' in data:
            actualizar_datos['contacto'] = data['contacto']
        if 'direccion' in data:
            actualizar_datos['direccion'] = data['direccion']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Propietario actualizado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Propietario no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar propietario
def eliminar_propietario(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Propietario eliminado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Propietario no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400