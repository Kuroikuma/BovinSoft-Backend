from flask import request, jsonify
from bson import ObjectId
from models.PremiumRequest import PremiumRequest

# Insertar premium_request
def insertar_premium_request(collection):
    try:
        data = request.get_json()
        premium_request = PremiumRequest(
            userId = data['userId'],
            requestDate = data.get('requestDate'),
            status = data['status'],
        )
        premium_request_data = premium_request.to_dict()
        collection.insert_one(premium_request_data)
        premium_request_data['_id'] = str(premium_request_data['_id'])
        premium_request_data['userId'] = str(premium_request_data['userId'])
        
        return jsonify({"Mensaje": "premium_request registrada exitosamente", "premium_request": premium_request_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar premium_requests
def mostrar_premium_requests(collection, id):
    try:
        premium_request = collection.find_one({"_id": ObjectId(id)})
        if premium_request:
            return jsonify({"premium_request": premium_request}), 200
        else:
            return jsonify({"Mensaje": "premium_request no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todas las premium_requests
def mostrar_todos_premium_requests(collection, collection_users):
    try:
        premium_requests = collection.find()
        premium_requests_list = []
        users_ids = []
        for premium_request in premium_requests:
            premium_request['_id'] = str(premium_request['_id'])
            users_ids.append(premium_request['userId'])
            premium_request['userId'] = str(premium_request['userId'])  # Convertir ObjectId a string
            premium_requests_list.append(premium_request)
        
        users = list(collection_users.find({"_id": {"$in": users_ids}}))
        
        print("hola")
        
        for premium_request_doc in premium_requests_list:
          user = next((user for user in users if user['_id'] == ObjectId(premium_request_doc['userId'])), None)
          premium_request_doc['userName'] = user['nombre']
          premium_request_doc['userEmail'] = user['email']  
        return jsonify({"premium_requests": premium_requests_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar premium_request
def actualizar_premium_request(collection, id, collection_users):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'status' in data:
            actualizar_datos['status'] = data['status']
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})
        
        user = collection_users.find_one({"_id": ObjectId(data['userId'])})
        
        if data['status'] == 'approved':
            user['tipoSuscripcion'] = 'premium'
            collection_users.update_one({"_id": ObjectId(data['userId'])}, {"$set": user})
            
        if result.matched_count > 0:
            return jsonify({"Mensaje": "premium_request actualizada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "premium_request no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar premium_request
def eliminar_premium_request(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "premium_request eliminada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "premium_request no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400