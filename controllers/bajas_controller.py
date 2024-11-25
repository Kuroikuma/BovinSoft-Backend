from flask import request, jsonify
from bson import ObjectId
from models.bajas import Bajas

def insertar_baja(collection):
    try:
        data = request.get_json()
        baja = Bajas(data['bovinoId'], data['fecha'], data.get('motivo'))
        result = collection.insert_one(baja.to_dic())
        return jsonify({'_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def mostrar_bajas(collection, page=1, per_page=20):
    try:
        skip = (page - 1) * per_page
        limit = per_page
        bajas = list(collection.find())
        for baja in bajas:
            baja['_id'] = str(baja['_id']) #convierte el ObjectId en un str
            baja['bovinoId'] = str(baja['bovinoId'])
            return jsonify(bajas)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
