from datetime import datetime
from bson import ObjectId

class Lotes:
    def __init__(self, nombre, ubicacion, asignable, propietarioId):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.asignable = asignable
        self.propietarioID = ObjectId(propietarioId)
        self._id = ObjectId()

    def to_dic(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "asignable": self.asignable,
            "propietarioID": self.propietarioID
        }