from datetime import datetime
from bson import ObjectId

class HistorialPeso:
    def __init__(self, bovinoId, fecha, peso):
        self.bovinoID = ObjectId(bovinoId)
        self.fecha = fecha
        self.peso = peso
        self._id = ObjectId()

    def to_dic(self):
        return {
            "_id": self._id,
            "bovinoId": self.bovinoID,
            "fecha": self.fecha,
            "peso": self.peso
        }