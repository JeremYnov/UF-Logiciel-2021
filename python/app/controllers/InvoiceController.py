from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Invoice import Invoice

class InvoiceController(Resource):
    def post(self):
        body = request.json

        invoice = Invoice.create(body)

        return Response(invoice.to_json(), mimetype="application/json", status=200)