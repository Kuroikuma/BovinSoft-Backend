from flask import request, jsonify
from bson import ObjectId
from models.CalendarioCuidados import CalendarioCuidados

# Insertar calendario_cuidado
def insertar_calendario_cuidado(collection):
    try:
        data = request.get_json()
        calendario_cuidado = CalendarioCuidados(
            bovinoId = data['bovinoId'],
            fechaProgramada = data.get('fechaProgramada'),
            actividad = data['actividad'],
            descripcion = data.get('descripcion'),
            estado = data.get('estado'),
            costoEstimado = data.get('costoEstimado'),
            titulo = data.get('titulo')  
        )
        calendario_cuidado_data = calendario_cuidado.to_dict()
        collection.insert_one(calendario_cuidado_data)
        calendario_cuidado_data['_id'] = str(calendario_cuidado_data['_id'])
        calendario_cuidado_data['bovinoId'] = str(calendario_cuidado_data['bovinoId'])
        
        return jsonify({"Mensaje": "calendario_cuidado registrada exitosamente", "calendario_cuidado": calendario_cuidado_data}), 201
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar calendario_cuidados
def mostrar_calendario_cuidados(collection, id):
    try:
        calendario_cuidado = collection.find_one({"_id": ObjectId(id)})
        if calendario_cuidado:
            return jsonify({"calendario_cuidado": calendario_cuidado}), 200
        else:
            return jsonify({"Mensaje": "calendario_cuidado no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Mostrar todas las calendario_cuidados
def mostrar_todos_calendario_cuidados(collection):
    try:
        calendario_cuidados = collection.find()
        calendario_cuidados_list = []
        for calendario_cuidado in calendario_cuidados:
            calendario_cuidado['_id'] = str(calendario_cuidado['_id'])  # Convertir ObjectId a string
            calendario_cuidado['bovinoId'] = str(calendario_cuidado['bovinoId'])  # Convertir ObjectId a string
            calendario_cuidados_list.append(calendario_cuidado)
        return jsonify({"calendario_cuidados": calendario_cuidados_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Actualizar calendario_cuidado
def actualizar_calendario_cuidado(collection, id):
    try:
        data = request.get_json()
        actualizar_datos = {}
        if 'fechaProgramada' in data:
            actualizar_datos['fechaProgramada'] = data['fechaProgramada']
        if 'motivo' in data:
            actualizar_datos['motivo'] = data['motivo']

        result = collection.update_one({"_id": ObjectId(id)}, {"$set": actualizar_datos})

        if result.matched_count > 0:
            return jsonify({"Mensaje": "calendario_cuidado actualizada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "calendario_cuidado no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400

# Eliminar calendario_cuidado
def eliminar_calendario_cuidado(collection, id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Mensaje": "calendario_cuidado eliminada exitosamente"}), 200
        else:
            return jsonify({"Mensaje": "calendario_cuidado no encontrada"}), 404
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400
      
def mostrar_calendario_cuidado_por_bovino_id(collection, collectionBovino, bovino_id):
    try:
        calendario_cuidados = collection.find({"bovinoId": ObjectId(bovino_id)})
        calendario_cuidados_list = []
        
        for cuidados in calendario_cuidados:
            cuidados['_id'] = str(cuidados['_id'])  # Convertir ObjectId a string
            cuidados['bovinoId'] = str(cuidados['bovinoId'])  # Convertir ObjectId a string
            calendario_cuidados_list.append(cuidados)
        
        return jsonify({"scheduledCare": calendario_cuidados_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400
      
def mostrar_calendario_cuidado_por_finca_id(collection, collectionBovino, finca_id):
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
            
        scheduled_care = collection.find({"bovinoId": {"$in": bovinos_ids}})
        
        scheduled_care_list = []
        for programmed_care in scheduled_care:
            programmed_care['_id'] = str(programmed_care['_id'])  # Convertir ObjectId a string
            programmed_care['bovinoId'] = str(programmed_care['bovinoId'])  # Convertir ObjectId a string
            scheduled_care_list.append(programmed_care)
          
        return jsonify({"scheduledCare": scheduled_care_list}), 200
    except Exception as e:
        return jsonify({"Mensaje": str(e)}), 400