from datetime import datetime
from bson import ObjectId

class HistorialSanitario:
    def __init__(self, bovinoId, fecha, descripcion, veterinario, tipo, medicamento=None ):
        self.bovinoId = ObjectId(bovinoId) # id del bovino
        self.fecha = fecha
        self.descripcion = descripcion
        self.veterinario = veterinario
        self.medicamento = medicamento if medicamento else None
        self.tipo = tipo
        self._id = ObjectId()
    
    def to_dic(self):
        return {
            "_id": self._id,
            "bovinoId": self.bovinoId,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "veterinario": self.veterinario,
            "medicamento": self.medicamento,
            "tipo": self.tipo
        }