from datetime import datetime
from bson import ObjectId

class HistorialSanitario:
    def __init__(self, bovinoId, fecha, descripcion, veterinario, medicamento, tipo):
        self.bovinoID = ObjectId(bovinoId) # id del bovino
        self.fecha = fecha
        self.descripcion = descripcion
        self.veterinario = veterinario
        self.medicamento = medicamento
        self.tipo = tipo
        self._id = ObjectId()
    
    def to_dic(self):
        return {
            "_id": self._id,
            "": self.bovinoID,
            "": self.fecha,
            "": self.descripcion,
            "": self.veterinario,
            "": self.medicamento,
            "": self.tipo
        }