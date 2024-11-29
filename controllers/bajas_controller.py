from flask import request, jsonify
from bson import ObjectId
from models.bajas import CalendarioCuidados

# Insertar baja
def insertar_baja(collection):
    try:
        data = request.get_json()
        baja = CalendarioCuidados(
            bovinoId=data['bovinoId'],
            fecha=data['fecha'],
            motivo=data.get('motivo')
        )
        baja_data = baja.to_dic()
        collection.insert_one(baja_data)
        return jsonify({"Mensaje": "Baja registrada exitosamente", "baja": baja_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar bajas
def mostrar_bajas(collection, id):
    try:
        baja = collection.find_one({"_id": ObjectId(id)})
        if baja:
            return jsonify({"baja": baja}), 200
        else:
            return jsonify({"Mensaje": "Baja no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todas las bajas
def mostrar_todas_bajas(collection):
    try:
        bajas = collection.find()
        bajas_list = []
        for baja in bajas:
            baja['_id'] = str(baja['_id'])  # Convertir ObjectId a string
            baja['bovinoId'] = str(baja['bovinoId'])  # Convertir ObjectId a string
            bajas_list.append(baja)
        return jsonify({"bajas": bajas_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar baja
def actualizar_baja(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'fecha' in data:
            actualizar_datos['fecha'] = data['fecha']
        if 'motivo' in data:
            actualizar_datos['motivo'] = data['motivo']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "Baja actualizada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Baja no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar baja
def eliminar_baja(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "Baja eliminada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "Baja no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400