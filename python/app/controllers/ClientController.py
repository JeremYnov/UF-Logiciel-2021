from flask import Response, request, jsonify, redirect
from flask_restful import Resource

import json

from app.models.Client import Client
from app.models.Invoice import Invoice

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
                    "firstName" : {
                        "type": "text",
                        "placeholder": "Enter firstName...",
                        "name":"firstName",
                        "label":"Firstname",
                        "value":client['firstName'],
                    },
                    "lastName" : {
                        "type": "text",
                        "placeholder": "Enter lastName...",
                        "name":"lastName",
                        "label":"Lastname",
                        "value":client['lastName'],
                    },
                    "email" : {
                        "type": "email",
                        "placeholder": "Enter email...",
                        "name":"email",
                        "label":"Email",
                        "value":client['email'],
                    }
                }
            } 

            return jsonify(result)
        
        if str(request.url_rule) == '/api/client/form':
            result = {
                "firstName" : {
                    "type": "text",
                    "placeholder": "Enter firstName...",
                    "name":"firstName",
                    "label":"Firstname",
                },
                "lastName" : {
                    "type": "text",
                    "placeholder": "Enter lastName...",
                    "name":"lastName",
                    "label":"Lastname",
                },
                "email" : {
                    "type": "email",
                    "placeholder": "Enter email...",
                    "name":"email",
                    "label":"Email",
                }
            }
            return jsonify(result)
        
        result = {
            'message': f"data client {client['id']} n'existe pas",
            'success': False,
        }
        return jsonify(result)

    def post(self):
        body = dict(request.form)
        client = Client.create(body)

        if not client:
            result = {
                'message': f"data client not create",
                'success': False,
            }
            return jsonify(result)

        result = {
            'message': f"data client created",
            'success': True,
            'result': client
        }
        return redirect('http://localhost:8080/clients')

    def put(self, id=""):
        body = dict(request.form)
        updated = Client.update(id, body)

        if updated["count"] == 0:
            result = {
                'message': f"data client {id} not update",
                'success': False,
            }
            return jsonify(result)

        result = {
            'message': f"data client {id} update",
            'path': {
                'path': f"/client/{id}",
                'name': "Client",
                'params': { 'id': id }
            },
            'success': True,
            'updated': updated
        }
        return jsonify(result)
    
    def delete(self, id=""):
        client = Client.deleteClient(id)

        clientsIsDelete = Invoice.isClientDelete(client)
        result = {
            "message": f"data client {id} not delete, le client est dans un invoice",
            "success": False,
            "inInvoice": False
        }

        if clientsIsDelete :
            client.delete()
            result["message"] = "la suppression a bien été faites"
            result["success"] = True
            result["inInvoice"] = True

        return jsonify(result)
