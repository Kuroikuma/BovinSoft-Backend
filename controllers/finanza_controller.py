from flask import request, jsonify
from models.finanza import Finanzas
from bson import ObjectId

# Insertar finanzas
def insertar_finanzas(collection):
    try:
        data = request.get_json()
        finanzas = Finanzas(
            bovinoId=data['bovinoId'],
            fecha=data['fecha'],
            tipo_gasto=data['tipo_gasto'],
            cantidad=data['cantidad'],
            descripcion=data['descripcion']
        )
        finanzas_data = finanzas.to_dic()
        collection.insert_one(finanzas_data)
        return jsonify({"Mensaje": "Finanzas registradas exitosamente", "finanzas": finanzas_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar finanzas
def mostrar_finanzas(collection, id):
    try:
        finanzas = collection.find_one({"_id": ObjectId(id)})
        if finanzas:
            return jsonify({"finanzas": finanzas}), 200
        else:
            return jsonify({"Mensaje": "Finanzas no encontradas"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todas las finanzas
def mostrar_todas_finanzas(collection):
    try:
        finanzas_list = []
        finanzas = collection.find()
        for item in finanzas:
            item['_id'] = str(item['_id'])  # Convertir ObjectId a string
            item['bovinoId'] = str(item['bovinoId'])  # Convertir ObjectId a string
            finanzas_list.append(item)
        return jsonify({"finanzas": finanzas_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar finanzas
def actualizar_finanzas(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'fecha' in data:
            actualizar_datos['fecha'] = data['fecha']
        if 'tipo_gasto' in data:
            actualizar_datos['tipo_gasto'] = data['tipo_gasto']
        if 'cantidad' in data:
            actualizar_datos['cantidad'] = data['cantidad']
        if 'descripcion' in data:
            actualizar_datos['descripcion'] = data['descripcion']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Finanzas actualizadas exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Finanzas no encontradas"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar finanzas
def eliminar_finanzas(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Finanzas eliminadas exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Finanzas no encontradas"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400