from flask import Response, request, jsonify, redirect
from flask_restful import Resource

import json

from app.models.Product import Product
from app.models.Invoice import Invoice

class ProductController(Resource):
    def get(self, id="", filename="") :
        if str(request.url_rule) == '/api/product/<string:id>':

            product = Product.getProduct(id)
            result = {
                "message": 'recuperation du produit' + str(product["name"]),
                "success": True,
                "count" : 1,
                "result": product,
                'form': {
                    "name" : {
                        "type": "text",
                        "placeholder": "Enter name...",
                        "name":"name",
                        "label":"Name",
                        "value":product['name']
                    },
                    "stock" : {
                        "type": "number",
                        "placeholder": "Enter stock...",
                        "name":"stock",
                        "label":"Stock",
                        "value":product['stock']
                    },
                    "picture" : {
                        "type": "file",
                        "placeholder": "Enter picture...",
                        "name":"picture",
                        "label":"Picture",
                    },
                    "price" : {
                        "type":"number", 
                        "step":"any",
                        "placeholder": "Enter price...",
                        "name":"price",
                        "label":"Price",
                        "value":product['price']
                    }
                }
            }

            return jsonify(result)
        
        elif str(request.url_rule) == '/api/products':

            products = Product.getAllProducts()
                        
            result = {
                "message": 'recuperation des produits',
                "success": True,
                "count" : len(products),
                "results": products,
                "unitName": "Product"
            }

            return jsonify(result)

        elif str(request.url_rule) == '/api/product/<string:id>/image/<string:filename>':
            return Product.getImage(id)

        elif str(request.url_rule) == '/api/product/form':
            result = {
                "name" : {
                    "type": "text",
                    "placeholder": "Enter name...",
                    "name":"name",
                    "label":"Name",
                },
                "stock" : {
                    "type": "number",
                    "placeholder": "Enter stock...",
                    "name":"stock",
                    "label":"Stock",
                },
                "picture" : {
                    "type": "file",
                    "placeholder": "Enter picture...",
                    "name":"picture",
                    "label":"Picture",
                },
                "price" : {
                    # "type": "float",
                    "type":"number", 
                    "step":"any",
                    "placeholder": "Enter price...",
                    "name":"price",
                    "label":"Price",
                }
            }

            return jsonify(result)
        
        return Response(status=404)

    def post(self):
        body = dict(request.form)
        picture = request.files['picture']

        product = Product.createProduct(body, picture)

        return redirect('http://localhost:8080/products')

    def put(self, id=""):
        body = dict(request.form)
        picture = ""

        if request.files:
            picture = request.files['picture']
       
        updated = Product.updateProduct(id, body, picture)
        
        if updated["count"] == 0:
            result = {
                'message': f"data produit {id} not update",
                'success': False
            }
            return jsonify(result)

        result = {
            'message': f"data produit {id} update",
            'path': {
                'path': f"/product/{id}",
                'name': "Product",
                'params': { 'id': id }
            },
            'success': True,
            'updated': updated
        }
        return jsonify(result)

    def delete(self, id=""):
        if str(request.url_rule) == '/api/product/<string:id>/delete':
            
            product = Product.deleteProduct(id)
            productIsDelete = Invoice.isProductDelete(product)
            result = {
                "message": "le produit ne peut pas être supprimer car il est dans un ou plusieurs invoice",
                "success": False,
                "inInvoice" : False
            }

            if not product:
                result["message"] = "le produit n'existe pas, il ne peut pas y avoir de suppresion"
                result["success"] = False

            if productIsDelete :
                product.delete()
                result["message"] = "la suppression a bien été faites"
                result["success"] = True
                result["inInvoice"] = True

            return jsonify(result)

        return Response(status=404)