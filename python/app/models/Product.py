import json, io
from flask import send_file

from datetime import datetime
from app.models import db

class Product(db.Document):
    meta = {'collection': 'Product'}
    name = db.StringField(required=True)
    stock = db.IntField(required=True)
    picture = db.FileField(required=True)
    price = db.FloatField(required=True)

    @staticmethod
    def createProduct(body, picture):
        try:
            product = Product.from_json(json.dumps(body), True)
            product.picture.put(picture, filename=picture.filename.replace(" ", "_"), content_type=picture.content_type)
            product.save()
        except Exception as error:
            print(error)

        return product

    @staticmethod
    def getProduct(id):
        try:
            product = Product.objects().get(id=str(id))
            data = {}
            data["id"] = str(product.id)
            data["name"] = product.name
            data["stock"] = product.stock
            data["price"] = product.price
            data["image"] = {}
            data["image"]["url"] = f"/api/product/{str(product.id)}/image/{product.picture.filename}"
            data["image"]["name"] = product.picture.filename

        except Exception as error:
            print(error)

        return data

    @staticmethod
    def getImage(id):
        try:
            product = Product.objects().get(id=id)
        
            file = send_file(io.BytesIO(product.picture.read()),
                     attachment_filename=product.picture.filename,
                     mimetype=product.picture.content_type)

        except Exception as error:
            print(error)

        return file

    @staticmethod
    def getAllProducts():
        try:
            products = Product.objects().all()
            listProducts = []
            for product in products :
                data = {}
                data["id"] = str(product.id)
                data["name"] = product.name
                data["stock"] = product.stock
                data["price"] = product.price
                data["image"] = {}
                data["image"]["url"] = f"/api/product/{str(product.id)}/image/{product.picture.filename}"
                data["image"]["name"] = product.picture.filename
                data["isDelete"] = False

                listProducts.append(data)
            
        except Exception as error:
            print(error)

        return listProducts

    @staticmethod
    def updateProduct(id, body, picture):
        try:
            updated = {
                "count": 0
            }

            product = Product.objects().get(id=id)

            if body["name"]:
                product.name = body["name"]
                updated["name"] = "updated"
                updated["count"] += 1
            if body["stock"]:
                product.stock = int(body["stock"])
                updated["stock"] = "updated"
                updated["count"] += 1
            if body["price"]:
                product.price = float(body["price"])
                updated["price"] = "updated"
                updated["count"] += 1
            if picture:
                product.picture.replace(picture, filename=picture.filename.replace(" ", "_"), content_type=picture.content_type)
                updated["picture"] = "updated"
                updated["count"] += 1

            product.save()    
        except Exception as error:
            print(error)

        return updated

    @staticmethod
    def deleteProduct(id):
        try:
            product = Product.objects().get(id=str(id))
            product.delete()
            
        except Exception as error:
            product = None
            print(error)

        return product