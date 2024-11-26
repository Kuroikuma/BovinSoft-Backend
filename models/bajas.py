from datetime import datetime
from bson import ObjectId

class Bajas:
    def __init__(self, bovinoId, fecha, motivo=None ):
        self.bovinoID = ObjectId(bovinoId) # Id del bovino
        self.fecha = fecha
        self.motivo = motivo
        self._id = ObjectId
    
    def to_dic(self):
        return {
            "_id": self._id,
            "bovinoId": self.bovinoID,
            "fecha": self.fecha,
            "motivo": self.motivo
        }
