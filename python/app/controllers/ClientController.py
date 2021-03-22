from flask import Response, request
from flask_restful import Resource

import json

from ..models.Client import Client

class ClientController(Resource):
    def get(self):
        # client = Client.objects().get(id="6058cf8a598e4d34ee3dee0f")
        body = request.json
        client = Client.objects().from_json(body)

        # client = Client.objects().exclude('id').to_json()
        # 6058cf8a598e4d34ee3dee0f
        print(client)
        print(client.id)
        print(client.firstName)
        print(client.lastName)
        print(client.to_mongo())


        return Response(client.to_json(), mimetype="application/json", status=200)

    def post(self):
        # client = Client({"firstName":"Louis", "lastName":"ardilly"})
        body = request.json
        print(type(body))
        print(type(json.dumps(body)))

        client = Client.from_json(json.dumps(body), True)


        client.save()

        return Response(client.to_json(), mimetype="application/json", status=200)

