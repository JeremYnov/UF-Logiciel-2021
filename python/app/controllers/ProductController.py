from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Product import Product


class ProductController(Resource):
    def get(self, id="") :
        if str(request.url_rule) == '/api/product/<string:id>':

            product = Product.getProduct(id)
            print(product)
            return jsonify(product)
        
        elif str(request.url_rule) == '/api/product/':

            product = Product.getAllProducts()
            return jsonify(product)
        
        return Response(status=404)

    def post(self, id=""):
        body = request.json

        if str(request.url_rule) == '/api/product/new':

            product = Product.createProduct(body)
            return Response(product.to_json(), mimetype="application/json", status=200)
        
        elif str(request.url_rule) == '/api/product/<string:id>/update':

            product = Product.updateProduct(id, body)
            return Response(product.to_json(), mimetype="application/json",status=200)
        
        return Response(status=404)