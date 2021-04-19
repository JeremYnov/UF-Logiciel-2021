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
                'unitName': "Client",
                'results': clients
            }

            return jsonify(result)

        if str(request.url_rule) == "/api/client/<string:id>":
            client = Client.findById(id)

            result = {
                'message': f"data client {client['id']}",
                'success': True,
                'result': client,
                'form': {
                    'firstName': "text",
                    'lastName': "text",
                    'email': "email",
                }
            }

            return jsonify(result)
        
        if str(request.url_rule) == '/api/client/form':
            result = {
                "firstName" : {
                    "type": "text",
                    "placeholder": "Enter firstName..."
                },
                "lastName" : {
                    "type": "text",
                    "placeholder": "Enter lastName..."
                },
                "picture" : {
                    "email": "email",
                    "placeholder": "Enter email..."
                }
            }

        result = {
            'message': f"data client {client['id']} n'existe pas",
            'success': False,
        }

        return jsonify(result)

    def post(self):
        body = request.json

        client = Client.create(body)

        if not client:
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
        if str(request.url_rule) == '/api/client/<string:id>/update':
            body = request.json
            
            updated = Client.update(id, body)

            if updated != 0:
                result = {
                    'message': f"data client {id} update",
                    'success': True,
                    'updated': updated
                }

                return jsonify(result)

            result = {
                'message': f"data client {id} not update",
                'success': False,
            }

            return jsonify(result)

        return Response(status=404)

    
    def delete(self, id=""):
        if str(request.url_rule) == '/api/client/<string:id>/delete':
            client = Client.delete(id)

            # if not client:
            #     result = {
            #         "message": f"data client not delete",
            #         "success": False
            #     }

            #     return jsonify(result)

            result = {
                "message": f"data client {id} delete",
                "success": True
            }

            return jsonify(result)

        return Response(status=404)
