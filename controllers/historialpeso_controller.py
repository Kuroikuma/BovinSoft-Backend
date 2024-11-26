from flask import request, jsonify
from models.historial_peso import HistorialPeso
from bson import ObjectId

# Insertar historial de peso
def insertar_historial_peso(collection):
    try:
        data = request.get_json()
        historial = HistorialPeso(
            bovinoId=data['bovinoId'],
            fecha=data['fecha'],
            peso=data['peso']
        )
        historial_data = historial.to_dic()
        collection.insert_one(historial_data)
        return jsonify({"Mensaje": "Historial de peso registrado exitosamente", "historial": historial_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar historial de peso
def mostrar_historial_peso(collection, id):
    try:
        historial = collection.find_one({"_id": ObjectId(id)})
        if historial:
            return jsonify({"historial": historial}), 200
        else:
            return jsonify({"Mensaje": "Historial de peso no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todos los historiales de peso
def mostrar_todos_historiales_peso(collection):
    try:
        historiales = collection.find()
        historiales_list = []
        for historial in historiales:
            historial['_id'] = str(historial['_id'])  # Convertir ObjectId a string
            historial['bovinoId'] = str(historial['bovinoId'])  # Convertir ObjectId a string
            historiales_list.append(historial)
        return jsonify({"historiales": historiales_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar historial de peso
def actualizar_historial_peso(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'fecha' in data:
            actualizar_datos['fecha'] = data['fecha']
        if 'peso' in data:
            actualizar_datos['peso'] = data['peso']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Historial de peso actualizado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Historial de peso no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar historial de peso
def eliminar_historial_peso(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Historial de peso eliminado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Historial de peso no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400