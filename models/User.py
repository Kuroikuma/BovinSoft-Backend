from datetime import datetime

from bson import ObjectId

##modelo de objeto usuario
class UserModel:
    def __init__(self, data):
        self.nombre = data.get('nombre', '')
        self.apellido = data.get('apellido', None)
        self.fecha_nacimiento = data.get('fecha_nacimiento', None)
        self.email = data.get('email', '')
        self.password = data.get('password', '')
        self.telefono = data.get('telefono', None)
        self.tipoSuscripcion = data.get('tipoSuscripcion', '') ## Ej: "básica", "premium"
        self.rol = data.get('rol', '') ## Ej: "admin", "ganadero"
        self.direccion = data.get('direccion', None)
        self.image = data.get('image', None)
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())
        self.fincaId = data.get('fincaId', None)
        self.pushToToken = data.get('pushToToken', None)
        self.status = data.get('status', '')
        self._id = ObjectId(data.get('_id', None))