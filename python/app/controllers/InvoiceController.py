from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Invoice import Invoice

class InvoiceController(Resource):
    def get(self, id="") :
        
        if str(request.url_rule) == '/api/invoices':

            invoices = Invoice.getAllInvoice()
            result = {
                "message": 'recuperation des factures',
                "success": True,
                "count" : len(invoices),
                "results": invoices,
                "unitName": "Invoice"
            }

            return jsonify(result)
        
        elif str(request.url_rule) == '/api/invoice/<string:id>' :
            invoice = Invoice.getInvoice(id)
            result = {
                "message": 'recuperation de la facture ' + str(invoice["id"]),
                "success": True,
                "count" : 1,
                "result": invoice
            }

            return jsonify(result)

        if str(request.url_rule) == '/api/invoice/form':
            result = {
                "client" : {
                    "type": "multiselect",
                    "placeholder": "Search client...",
                    "name":"clients",
                    "label":"Client",
                    "multiple" : False
                },
                "products" : {
                    "type": "multiselect",
                    "placeholder": "Search products...",
                    "name":"products",
                    "label":"Products",
                    "multiple" : True
                }
            }
            return jsonify(result)

        return Response(status=404)
    def post(self):
        body = request.json

        invoice = Invoice.create(body)

        return Response(invoice.to_json(), mimetype="application/json", status=200)
    

    def delete(self, id=""):
        if str(request.url_rule) == '/api/invoice/<string:id>/delete':
            
            invoice = Invoice.deleteInvoice(id)
            result = {
                "message": "la suppresion a bien été faites",
                "success": True
            }
            if not invoice:
                result["message"] = "le produit n'existe pas, il ne peut pas y avoir de suppresion"
                result["success"] = False
            return jsonify(result)

        return Response(status=404)

    def put(self, id=""):
        body = request.json
        updated = Invoice.update(id, body)

        if updated["count"] == 0:
            result = {
                'message': f"data invoice {id} not update",
                'success': False,
            }
            return jsonify(result)

        result = {
            'message': f"data invoice {id} update",
            'path': {
                'path': f"/invoice/{id}",
                'name': "Invoice",
                'params': { 'id': id }
            },
            'success': True,
            'updated': updated
        }

        return jsonify(result)