from flask import Response, request, jsonify, redirect
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

            productsId = []
            for item in invoice["products"]:
                productsId.append(item['id']) 

            result = {
                "message": 'recuperation de la facture ' + str(invoice["id"]),
                "success": True,
                "count": 1,
                "result": invoice,
                "form": {
                    "client": {
                        "type": "multiselect",
                        "placeholder": "Search client...",
                        "name":"clients",
                        "label":"Client",
                        "multiple": False,
                        "value": invoice["client"]["id"]
                    },
                    "products": {
                        "type": "multiselect",
                        "placeholder": "Search products...",
                        "name":"products",
                        "label":"Products",
                        "multiple": True,
                        "value": productsId
                    },
                    "isPaid": {
                        "type": "multiselect",
                        "placeholder": "IsPaid...",
                        "name":"isPaid",
                        "label":"IsPaid",
                        "multiple": False,
                        "value": str(invoice["isPaid"])
                    }
                }
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
        req = request.form
        body = {
            'client': "",
            'products': []
        }
        body['client'] = req['client']
        body['products'] = req['products'].split(',')

        invoice = Invoice.create(body)

        return redirect('http://localhost:8080/invoices')

    def delete(self, id=""):
        if str(request.url_rule) == '/api/invoice/<string:id>/delete':
            
            invoice = Invoice.deleteInvoice(id)
            result = {
                "message": "la suppresion a bien ??t?? faites",
                "success": True
            }
            if not invoice:
                result["message"] = "le produit n'existe pas, il ne peut pas y avoir de suppresion"
                result["success"] = False
            return jsonify(result)

        return Response(status=404)

    def put(self, id=""):
        req = request.form
        print(req)
        body = {
            'client': "",
            'products': []
        }
        body['client'] = req['client']
        body['products'] = req['products'].split(',')
        if req['isPaid'] == "False":
            body["isPaid"] = False
        else:    
            body["isPaid"] = True
        print(body)
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