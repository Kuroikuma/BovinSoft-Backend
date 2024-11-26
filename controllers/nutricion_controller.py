from flask import request, jsonify
from models.nutricion import Nutricion
from bson import ObjectId

# Insertar nutrición
def insertar_nutricion(collection):
    try:
        data = request.get_json()
        nutricion = Nutricion(
            bovinoId=data['bovinoId'],
            fecha=data['fecha'],
            tipo_alimento=data['tipo_alimento'],
            cantidad=data['cantidad'],
            observaciones=data['observaciones']
        )
        nutricion_data = nutricion.to_dic()
        collection.insert_one(nutricion_data)
        return jsonify({"Mensaje": "Nutrición registrada exitosamente", "nutricion": nutricion_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar nutrición
def mostrar_nutricion(collection, id):
    try:
        nutricion = collection.find_one({"_id": ObjectId(id)})
        if nutricion:
            return jsonify({"nutricion": nutricion}), 200
        else:
            return jsonify({"Mensaje": "Nutrición no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todas las entradas de nutrición
def mostrar_toda_nutricion(collection):
    try:
        registros = collection.find()
        nutricion_list = []
        for registro in registros:
            registro['_id'] = str(registro['_id'])  # Convertir ObjectId a string
            registro['bovinoId'] = str(registro['bovinoId'])  # Convertir ObjectId a string
            nutricion_list.append(registro)
        return jsonify({"nutricion": nutricion_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar nutrición
def actualizar_nutricion(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'fecha' in data:
            actualizar_datos['fecha'] = data['fecha']
        if 'tipo_alimento' in data:
            actualizar_datos['tipo_alimento'] = data['tipo_alimento']
        if 'cantidad' in data:
            actualizar_datos['cantidad'] = data['cantidad']
        if 'observaciones' in data:
            actualizar_datos['observaciones'] = data['observaciones']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Nutrición actualizada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Registro de nutrición no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar registro de nutrición
def eliminar_nutricion(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Registro de nutrición eliminado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Registro de nutrición no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400
