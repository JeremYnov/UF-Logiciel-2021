import json

from datetime import datetime
from app.models import db

class Client(db.Document):
    meta = {'collection': 'Client'}
    firstName = db.StringField(required=True)
    lastName = db.StringField(required=True)
    email = db.EmailField(required=True)
    creation = db.DateTimeField(required=True, default=datetime.now())

    @staticmethod
    def createClient(body):
        try:
            client = Client.from_json(json.dumps(body), True)
            client.save()
        except Exception as error:
            print(error)

        return client