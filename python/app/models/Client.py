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
    def findAll():
        try:
            clients = Client.objects.all()
            results = []

            for client in clients:
                data = {}
                data['id'] = str(client.id)
                data['firstName'] = client.firstName
                data['lastName'] = client.lastName
                data['email'] = client.email
                data['creation'] = client.creation.strftime('%d/%m/%Y')

                results.append(data)
                
        except Exception as error:
            client = None

        return results

    @staticmethod
    def findById(id):
        try:
            client = Client.objects.get(id=id)

            data = {}
            data['id'] = str(client.id)
            data['firstName'] = client.firstName
            data['lastName'] = client.lastName
            data['email'] = client.email
            data['creation'] = client.creation.strftime('%d/%m/%Y')

        except Exception as error:
            client = None

        return data


    @staticmethod
    def create(body):
        try:
            client = Client.from_json(json.dumps(body), True)
            client.save()
        except Exception as error:
            print(error)
            client = None

        return client

    @staticmethod
    def update(id, body):
        try:
            updated = {
                "count": 0
            }

            client = Client.objects().get(id=id)

            if body["firstName"]:
                client.firstName = body["firstName"]
                updated["firstName"] = "updated"
                updated["count"] += 1

            if body["lastName"]:
                client.lastName = body["lastName"]
                updated["lastName"] = "lastName"
                updated["count"] += 1

            if body["email"]:
                client.email = body["email"]   
                updated["email"] = "email"
                updated["count"] += 1

            client.save()

        except Exception as error:
            print(error)

        return updated
    
    @staticmethod
    def delete(id):
        try:
            client = Client.objects(id=id)
            client.delete()
            
        except Exception as error:
            client = None

        return client