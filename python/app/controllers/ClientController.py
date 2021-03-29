from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Client import Client

class ClientController(Resource):
    def get(self):
        client = Client.objects().get(id="6058cf8a598e4d34ee3dee0f")
        body = request.json
        # client = Client.objects().from_json(body)

        # client = Client.objects().exclude('id').to_json()
        print(client)
        print(client.id)
        print(client.firstName)
        print(client.lastName)
        print(client.to_mongo())


        return Response(client.to_json(), mimetype="application/json", status=200)

    def post(self, id):
        body = request.json

        print(request.url_rule)

        if request.url_rule == '/api/client/new':
            client = Client.createClient(body)

            return Response(client.to_json(), mimetype="application/json", status=200)

        # elif request.url_rule == '/api/client/<int:id>/update':


        #     message = jsonify(error=True)
        #     print(message)


        #     return Response(message, mimetype="application/json",status=200)
        
        return Response(status=404)
