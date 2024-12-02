from datetime import datetime
from bson import ObjectId

class PremiumRequest:
    def __init__(self, userId, status, requestDate):
        self.userId = ObjectId(userId)  # ID del bovino
        self.requestDate = requestDate
        self.responseDate = None
        self.status = status
        self._id = ObjectId()

    def to_dict(self):
        return {
            "_id": self._id,
            "userId": self.userId,
            "requestDate": self.requestDate,
            "status": self.status,
            "responseDate": self.responseDate
        } 