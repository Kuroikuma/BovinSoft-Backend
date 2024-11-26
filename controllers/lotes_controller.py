from flask import request, jsonify
from models.lotes import Lotes
from bson import ObjectId

# Insertar lote
def insertar_lote(collection):
    try:
        data = request.get_json()
        lote = Lotes(
            nombre=data['nombre'],
            ubicacion=data['ubicacion'],
            asignable=data['asignable'],
            propietarioId=data['propietarioId']
        )
        lote_data = lote.to_dic()
        collection.insert_one(lote_data)
        return jsonify({"Mensaje": "Lote registrado exitosamente", "lote": lote_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar lote
def mostrar_lote(collection, id):
    try:
        lote = collection.find_one({"_id": ObjectId(id)})
        if lote:
            return jsonify({"lote": lote}), 200
        else:
            return jsonify({"Mensaje": "Lote no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todos los lotes
def mostrar_todos_lotes(collection):
    try:
        lotes = collection.find()
        lotes_list = []
        for lote in lotes:
            lote['_id'] = str(lote['_id'])  # Convertir ObjectId a string
            lote['propietarioId'] = str(lote['propietarioId'])  # Convertir ObjectId a string
            lotes_list.append(lote)
        return jsonify({"lotes": lotes_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar lote
def actualizar_lote(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'nombre' in data:
            actualizar_datos['nombre'] = data['nombre']
        if 'ubicacion' in data:
            actualizar_datos['ubicacion'] = data['ubicacion']
        if 'asignable' in data:
            actualizar_datos['asignable'] = data['asignable']
        if 'propietarioId' in data:
            actualizar_datos['propietarioId'] = ObjectId(data['propietarioId'])

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Lote actualizado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Lote no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar lote
def eliminar_lote(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Lote eliminado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Lote no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400