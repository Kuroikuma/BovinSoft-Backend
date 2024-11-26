from datetime import datetime
from bson import ObjectId

class Finanzas:
    def __init__(self, bovinoId, fecha, tipo_gasto, cantidad, descripcion):
        self.bovinoID = ObjectId(bovinoId)  # Id del bovino
        self.fecha = fecha
        self.tipo_gasto = tipo_gasto
        self.cantidad = cantidad
        self.descripcion = descripcion
        self._id = ObjectId()  # ID generado automáticamente para las finanzas

    def to_dic(self):
        return {
            "_id": self._id,
            "bovinoId": self.bovinoID,
            "fecha": self.fecha,
            "tipo_gasto": self.tipo_gasto,
            "cantidad": self.cantidad,
            "descripcion": self.descripcion
        }
