from flask import request, jsonify
from models.historial_sanitario import HistorialSanitario
from bson import ObjectId

# Insertar historial sanitario
def insertar_historial_sanitario(collection):
    try:
        data = request.get_json()
        historial = HistorialSanitario(
            bovinoId=data['bovinoId'],
            fecha=data['fecha'],
            descripcion=data['descripcion'],
            veterinario=data['veterinario'],
            medicamento=data['medicamento']
        )
        historial_data = historial.to_dic()
        collection.insert_one(historial_data)
        return jsonify({"Mensaje": "Historial sanitario registrado exitosamente", "historial": historial_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar historial sanitario
def mostrar_historial_sanitario(collection, id):
    try:
        historial = collection.find_one({"_id": ObjectId(id)})
        if historial:
            return jsonify({"historial": historial}), 200
        else:
            return jsonify({"Mensaje": "Historial sanitario no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todos los historiales sanitarios
def mostrar_todos_historiales_sanitarios(collection):
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

# Actualizar historial sanitario
def actualizar_historial_sanitario(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'fecha' in data:
            actualizar_datos['fecha'] = data['fecha']
        if 'descripcion' in data:
            actualizar_datos['descripcion'] = data['descripcion']
        if 'veterinario' in data:
            actualizar_datos['veterinario'] = data['veterinario']
        if 'medicamento' in data:
            actualizar_datos['medicamento'] = data['medicamento']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Historial sanitario actualizado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Historial sanitario no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar historial sanitario
def eliminar_historial_sanitario(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Historial sanitario eliminado exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Historial sanitario no encontrado"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400