from datetime import datetime
from bson import ObjectId

class Reproduccion:
    def __init__(self, bovinoId, fechaServicio=None, tipoServicio=None, padreId=None, confirmacionGestacion=None, fechaParto=None, estado='Pre Estrus', criaId=None):
        self._id = ObjectId()  # MongoDB genera un ID único automáticamente
        self.bovinoId = ObjectId(bovinoId)  # ID del bovino
        self.fechaServicio = fechaServicio if fechaServicio else None  # Fecha del servicio (opcional)
        self.tipoServicio = tipoServicio if tipoServicio else None  # Tipo de servicio (opcional)
        self.padreId = ObjectId(padreId) if padreId else None  # ID del padre (opcional)
        self.confirmacionGestacion = confirmacionGestacion
        self.fechaParto = fechaParto
        self.estado = estado
        self.criaId = ObjectId(criaId) if criaId else None  # ID de la cría (opcional)
        self.fechaCreacion = datetime.utcnow()  # Fecha de creación en UTC

    def to_dict(self):
        return {
            "_id": self._id,
            "bovinoId": self.bovinoId,
            "fechaServicio": self.fechaServicio,
            "tipoServicio": self.tipoServicio,
            "padreId": self.padreId,
            "confirmacionGestacion": self.confirmacionGestacion,
            "fechaParto": self.fechaParto,
            "estado": self.estado,
            "criaId": self.criaId,
            "fechaCreacion": self.fechaCreacion
        }
