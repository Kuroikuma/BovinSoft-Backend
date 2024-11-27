from flask import jsonify, request
from bson.json_util import dumps
from .model import ReproductiveEvent

def create_event(db):
    """Crear un nuevo evento reproductivo"""
    data = request.get_json()
    event_model = ReproductiveEvent(db)
    result = event_model.create(data)
    return jsonify({"message": "Evento creado", "id": str(result.inserted_id)}), 201

def create_many_events(db):
    """Crear múltiples eventos reproductivos"""
    data = request.get_json()  # Una lista de eventos
    event_model = ReproductiveEvent(db)
    result = event_model.create_many(data)
    return jsonify({"message": "Eventos creados", "ids": [str(id) for id in result.inserted_ids]}), 201

def get_all_events(db):
    """Obtener todos los eventos reproductivos"""
    event_model = ReproductiveEvent(db)
    events = event_model.get_all()
    return jsonify(events=dumps(events)), 200

def get_event_by_id(db, event_id):
    """Obtener un evento reproductivo por ID"""
    event_model = ReproductiveEvent(db)
    event = event_model.get_by_id(event_id)
    if event:
        return jsonify(event=dumps(event)), 200
    return jsonify({"error": "Evento no encontrado"}), 404

def get_events_by_reproductive_id(db, cattle_id):
    """Obtener todos los eventos reproductivos de un ganado"""
    event_model = ReproductiveEvent(db)
    events = event_model.get_event_by_reproductive_id(cattle_id)
    return jsonify(events=dumps(events)), 200

def update_event(db, event_id):
    """Actualizar un evento reproductivo"""
    data = request.get_json()
    event_model = ReproductiveEvent(db)
    result = event_model.update(event_id, data)
    if result.modified_count:
        return jsonify({"message": "Evento actualizado"}), 200
    return jsonify({"error": "Evento no encontrado"}), 404

def delete_event(db, event_id):
    """Eliminar un evento reproductivo"""
    event_model = ReproductiveEvent(db)
    result = event_model.delete(event_id)
    
    if result.deleted_count:
        return jsonify({"message": "Evento eliminado"}), 200
    return jsonify({"error": "Evento no encontrado"}), 404
  
def get_event_by_bovino_id(db, bovino_id):
    """Obtener todos los eventos reproductivos de un bovino"""
    event_model = ReproductiveEvent(db)
    
    bovino = event_model.get_bovino_by_id(bovino_id)
    
    reproducciones = event_model.get_reproductive_by_bovino_id(bovino_id)
    reproducciones_ids = [str(doc['_id']) for doc in reproducciones]
    
    for reproduccion in reproducciones:
      reproduccion["_id"] = str(reproduccion["_id"])
      reproduccion["id"] = str(reproduccion["_id"])
      reproduccion["bovinoId"] = str(reproduccion["bovinoId"])
    
    events = event_model.get_event_by_reproductive_ids(reproducciones_ids)
    
    events_by_reproductive = {}
    for event in events:
        event["_id"] = str(event["_id"])
        event["id"] = str(event["_id"])
        reproductive_id = event["reproductiveId"]
        if reproductive_id not in events_by_reproductive:
                events_by_reproductive[reproductive_id] = []
        events_by_reproductive[reproductive_id].append(event)
    
    for reproduccione in reproducciones:
            event_by_reproductive = events_by_reproductive.get(reproduccione['_id'], {})
            reproduccione["events"] = event_by_reproductive
            reproduccione["name"] = bovino["nombre"]
            
    return jsonify(reproducciones), 200
  
def get_reproductive_by_finca_id(db, finca_id):
    """Obtiene todos los eventos reproductivos de una finca"""
    event_model = ReproductiveEvent(db)
    bovinos = event_model.get_bovino_by_finca_id(finca_id)
    reproductives = event_model.get_reproductive_by_bovino_ids([bovino['_id'] for bovino in bovinos])
    
    for reproduccion in reproductives:
      reproduccion["_id"] = str(reproduccion["_id"])
      reproduccion["id"] = str(reproduccion["_id"])
    
    events = event_model.get_event_by_reproductive_ids([reproductive['_id'] for reproductive in reproductives])
    
    events_by_reproductive = {}
    for event in events:
        event["_id"] = str(event["_id"])
        event["id"] = str(event["_id"])
        reproductive_id = event["reproductiveId"]
        if reproductive_id not in events_by_reproductive:
                events_by_reproductive[reproductive_id] = []
        events_by_reproductive[reproductive_id].append(event)
    
    for reproduccione in reproductives:
            
            event_by_reproductive = events_by_reproductive.get(reproduccione['_id'], {})
            if not event_by_reproductive:
              event_by_reproductive = []
            reproduccione["events"] = event_by_reproductive
            reproduccione["name"] = next((bovino for bovino in bovinos if bovino['_id'] == reproduccione['bovinoId']), None)['nombre']
            reproduccione["bovinoId"] = str(reproduccione["bovinoId"])
    
        
    return jsonify(reproductives), 200	