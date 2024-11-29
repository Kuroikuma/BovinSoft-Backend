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
            medicamento=data['medicamento'],
            tipo=data['tipo'],
        )
        historial_data = historial.to_dic()
        collection.insert_one(historial_data)
        
        historial_data['_id'] = str(historial_data['_id'])
        historial_data['bovinoId'] = str(historial_data['bovinoId'])
        
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
      
def mostrar_historial_sanitario_por_bovino_id(collection,collectionBovino, bovino_id):
    try:
        bovino = collectionBovino.find_one({"_id": ObjectId(bovino_id)})
        if bovino is None:
          return jsonify({"Mensaje": "Bovino no encontrado"}), 404
        
        historiales = collection.find({"bovinoId": ObjectId(bovino_id)})
        historiales_list = []
        
        for historial in historiales:
            historial['_id'] = str(historial['_id'])  # Convertir ObjectId a string
            historial['bovinoId'] = str(historial['bovinoId'])  # Convertir ObjectId a string
            historiales_list.append(historial)
        
        bovino['careHistory'] = historiales_list
        bovino['_id'] = str(bovino['_id'])  # Convertir ObjectId a string
        bovino['fincaId'] = str(bovino['fincaId'])  # Convertir ObjectId a string
          
        return jsonify({"historiales": bovino}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400
      
def mostrar_historial_sanitario_por_finca_id(collection, collectionBovino, finca_id):
    try:
        bovinos_list = []
        bovinos_ids = []
        
        bovinos = collectionBovino.find({"fincaId": ObjectId(finca_id)})
        if bovinos is None:
          return jsonify({"Mensaje": "Finca no encontrada"}), 404
        
        for item in bovinos:
            bovinos_ids.append(item['_id'])
            item['_id'] = str(item['_id'])  # Convertir ObjectId a string
            item['fincaId'] = str(item['fincaId'])  # Convertir ObjectId a string
            bovinos_list.append(item)
            
        
        historiales = collection.find({"bovinoId": {"$in": bovinos_ids}})
        
        historiales_por_bovinos = {}
        for historial in historiales:
            historial['_id'] = str(historial['_id'])  # Convertir ObjectId a string
            historial['bovinoId'] = str(historial['bovinoId'])  # Convertir ObjectId a string
            bovino_id = historial["bovinoId"]
            if bovino_id not in historiales_por_bovinos:
                historiales_por_bovinos[bovino_id] = []
            historiales_por_bovinos[bovino_id].append(historial)
            
        for bovino in bovinos_list:
            historiales_por_bovino = historiales_por_bovinos.get(bovino['_id'], [])
            bovino['careHistory'] = historiales_por_bovino
            bovino['_id'] = str(bovino['_id'])  # Convertir ObjectId a string
            bovino['fincaId'] = str(bovino['fincaId'])  # Convertir ObjectId a string 
          
        return jsonify({"historiales": bovinos_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400