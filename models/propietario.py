from datetime import datetime
from bson import ObjectId

class Propietario:
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion
        self._id = ObjectId()

    def to_dic(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "contacto": self.contacto,
            "direccion": self.direccion
        }