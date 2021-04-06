from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Client import Client

class ClientController(Resource):
    def get(self, id=""):
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

        result = {
            'message': f"data client {client['id']} n'existe pas",
            'success': False,
        }

        return jsonify(result)

    def post(self):
        body = request.json

        client = Client.create(body)

        if client != 500:
            result = {
                'message': f"data client created",
                'success': True,
                'result': client
            }

            return jsonify(result)

        result = {
            'message': f"data client not create",
            'success': False,
        }

        return jsonify(result)
        

    def put(self, id=""):
        body = request.json
        
        updated = Client.update(id, body)

        if updated != 0:
            result = {
                'message': f"data client {id} update",
                'success': True,
                'updatec': updated
            }

            return jsonify(result)

        result = {
            'message': f"data client {id} not update",
            'success': False,
        }

        return jsonify(result)
