from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Product import Product


class ProductController(Resource):
    def get(self, id="") :
        if str(request.url_rule) == '/api/product/<string:id>':

            product = Product.getProduct(id)
            result = {
                "message": 'recuperation du produit' + str(product["name"]),
                "success": True,
                "count" : 1,
                "result": product
            }

            return jsonify(result)
        
        elif str(request.url_rule) == '/api/products':

            product = Product.getAllProducts()
            result = {
                "message": 'recuperation des produits',
                "success": True,
                "count" : len(product),
                "results": product
            }

            return jsonify(result)
        
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