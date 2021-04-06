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

            print(client.to_mongo())
        except Exception as error:
            print(error)

        return client

    @staticmethod
    def update(id, body):
        try:
            # print(body)
            # client2 = Client.from_json(json.dumps(body))
            # print(client2.to_json())
        
            client = Client.objects.get(id=id)
            print(client.to_json())

            
            client = Client.objects(id=id).update(firstName=body['firstName'])
            client = Client.objects(id=id).update(lastName=body['lastName'])
            client = Client.objects(id=id).update(email=body['email'])


       
            print(client.to_json())
        except Exception as error:
            print(error)

            return 0

        return client