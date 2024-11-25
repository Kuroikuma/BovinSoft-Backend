from flask import request, jsonify
from bson import ObjectId
from models.Reproduccion import Reproduccion

def insertar_reproduccion(collection):
    try:
        data = request.get_json()
        reproduccion = Reproduccion(**data) # crear un objeto reproduccion apartir de los datos json
        result =  collection.insert_one(reproduccion.to_dict())
        return jsonify({'_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def obtener_reproduccion(collection, reproduccion_id):
    try:
        reproduccion = collection.find_one({"_id": ObjectId(reproduccion_id)})
        if reproduccion:
            return jsonify(reproduccion), 200
        else:
            return jsonify({"error": "Reproduccion no encontrada"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def actualizar_reproduccion(collection, reproduccion_id):
    try:
        data = request.get_json()
        # para evitar actualizar el _id
        if "_id" in data:
            del data["_id"]
        result = collection.update_one({"_id": ObjectId(reproduccion_id)}, {"$set": data})
        if result.modified_count > 0:
            return jsonify({"message": "Reproduccion actualizada correctamente"}), 200
        else:
            return jsonify({"error": "Reproduccion no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def eliminar_reproduccion(collection, reproduccion_id):
    try:
        result = collection.delete_one({"_id": ObjectId(reproduccion_id)})
        if result.delete_count > 0:
            return jsonify({"message": "Reproduccion eliminada correctamente"}), 200
        else:
            return jsonify({"error": "Reproduccion no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500