from flask import current_app
from bson.objectid import ObjectId

class ReproductiveEvent:
    def __init__(self, db):
        self.collection = db("reproductive_events")
        self.collectionBovinos = db("bovinos")
        self.collectionReproductives = db("reproduccion")

    def create(self, event):
        """Inserta un evento reproductivo en la base de datos"""
        return self.collection.insert_one(event)

    def create_many(self, events):
        """Inserta múltiples eventos reproductivos en la base de datos"""
        return self.collection.insert_many(events)

    def get_all(self):
        """Obtiene todos los eventos reproductivos"""
        return list(self.collection.find())

    def get_by_id(self, event_id):
        """Obtiene un evento reproductivo por ID"""
        return self.collection.find_one({"_id": ObjectId(event_id)})

    def get_event_by_reproductive_id(self, reproductiveId):
        """Obtiene todos los eventos reproductivos de un ganado específico por cattleId"""
        return list(self.collection.find({"reproductiveId": reproductiveId}))

    def update(self, event_id, updates):
        """Actualiza un evento reproductivo por ID"""
        return self.collection.update_one(
            {"_id": ObjectId(event_id)}, {"$set": updates}
        )

    def delete(self, event_id):
        """Elimina un evento reproductivo por ID"""
        return self.collection.delete_one({"_id": ObjectId(event_id)})
  
    def get_bovino_by_id(self, bovino_id):
        """Obtiene un bovino por ID"""
        return self.collectionBovinos.find_one({"_id": ObjectId(bovino_id)})
      
    def get_reproductive_by_bovino_id(self, bovino_id):
        """Obtiene todos las reproducciones de un bovino"""
        return list(self.collectionReproductives.find({"bovinoId": ObjectId(bovino_id)}))
      
    def get_reproductive_by_bovino_ids(self, bovino_ids):
        """Obtiene todos las reproducciones de varios bovinos"""
        return list(self.collectionReproductives.find({"bovinoId": {"$in": bovino_ids}}))
      
    def get_event_by_reproductive_ids(self, ids):
        """Obtiene todos los eventos reproductivos de un ganado específico por cattleId"""
        return list(self.collection.find({"reproductiveId": {"$in": ids}}))
      
    def get_bovino_by_finca_id(self, finca_id):
        """Obtiene todos los bovinos de una finca"""
        return list(self.collectionBovinos.find({"fincaId": ObjectId(finca_id)}))
