from flask import Response, request, jsonify
from flask_restful import Resource

import json

from app.models.Product import Product

class ProductController(Resource):
    def get(self, id="", filename="") :
        if str(request.url_rule) == '/api/product/<string:id>':

            product = Product.getProduct(id)
            result = {
                "message": 'recuperation du produit' + str(product["name"]),
                "success": True,
                "count" : 1,
                "result": product,
                "form": {
                    "name" : "text",
                    "stock" : "number",
                    "picture" : "file",
                    "price" : "float"
                }
            }

            return jsonify(result)
        
        elif str(request.url_rule) == '/api/products':

            product = Product.getAllProducts()
            result = {
                "message": 'recuperation des produits',
                "success": True,
                "count" : len(product),
                "results": product,
                "unitName": "Product"
            }

            return jsonify(result)

        elif str(request.url_rule) == '/api/product/<string:id>/image/<string:filename>':
            return Product.getImage(id)
        
        return Response(status=404)

    def post(self):
        body = dict(request.form)
        picture = request.files['picture']

        product = Product.createProduct(body, picture)

        return Response(product.to_json(), mimetype="application/json", status=200)

    def put(self, id=""):
        body = dict(request.form)
        picture = request.files['picture']

        product = Product.updateProduct(id, body, picture)
        result = {
            "message" : f"le produit {id} a été modifié"
        }
        return jsonify(result)
    
    def delete(self, id=""):
        if str(request.url_rule) == '/api/product/<string:id>/delete':
            
            product = Product.deleteProduct(id)
            result = {
                "message": "la suppresion a bien été faites",
                "success": True
            }
            if not product:
                result["message"] = "le produit n'existe pas, il ne peut pas y avoir de suppresion"
                result["success"] = False
            return jsonify(result)

        return Response(status=404)