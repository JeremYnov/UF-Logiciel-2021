from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Client import Client

class ClientController(Resource):
    def get(self, id=""):
        print(request.url_rule)

            # client = Client.objects().get(id="6061ab85c4736bed637d552c")
            # body = request.json
            # client = Client.objects().from_json(body)

            # client = Client.objects().exclude('id').to_json()

        if str(request.url_rule) == "/api/clients":
            clients = Client.findAll()

            result = {
                'message': "liste de tout les clients",
                'success': True,
                'results': clients
            }

            return jsonify(result)

        if str(request.url_rule) == "/api/client/<string:id>":
            client = Client.findById(id)

            result = {
                'message': f"data client {client['id']}",
                'success': True,
                'result': client
            }

            return jsonify(result)

        return Response(status=404)

    def post(self, id=""):
        body = request.json

        if str(request.url_rule) == '/api/client/new':
            client = Client.createClient(body)

            return Response(client.to_json(), mimetype="application/json", status=200)

        if str(request.url_rule) == '/api/client/<int:id>/update':

            message = jsonify(error=True)
            print(message)

            return message
        
        return Response(status=404)
