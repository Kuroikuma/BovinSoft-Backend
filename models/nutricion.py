from datetime import datetime
from bson import ObjectId

class Nutricion:
    def __init__(self, bovinoId, fecha, tipo_alimento, cantidad, observaciones):
        self.bovinoID = ObjectId(bovinoId)
        self.fecha = fecha
        self.tipo_alimento = tipo_alimento
        self.cantidad = cantidad
        self.observaciones = observaciones
        self._id = ObjectId()

    def to_dic(self):
        return {
            "_id": self._id,
            "bovinoId": self.bovinoID,
            "fecha": self.fecha,
            "tipo_alimento": self.tipo_alimento,
            "cantidad": self.cantidad,
            "observacion": self.observaciones
        }