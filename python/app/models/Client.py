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
            print(error)

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
            print(error)

        return data


    @staticmethod
    def create(body):
        try:
            client = Client.from_json(json.dumps(body), True)
            client.save()
            
        except Exception as error:
            return 500

        return client

    @staticmethod
    def update(id, body):
        updated = {}
        count = 0

        try:
            firstName = Client.objects(id=id).update(firstName=body['firstName'])
            updated['firstName'] = firstName
            count += 1

        except Exception as error:
            updated['firstName'] = 0

        try:
            lastName = Client.objects(id=id).update(lastName=body['lastName'])
            updated['lastName'] = lastName
            count += 1

        except Exception as error:
            updated['lastName'] = 0

        try:
            email = Client.objects(id=id).update(email=body['email'])
            updated['email'] = email
            count += 1

        except Exception as error:
            updated['email'] = 0

        if count == 0:
            return count

        return updated