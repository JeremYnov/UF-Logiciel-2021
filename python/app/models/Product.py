import json

from datetime import datetime
from app.models import db

class Product(db.Document):
    meta = {'collection': 'Product'}
    name = db.StringField(required=True)
    stock = db.IntField(required=True)
    picture = db.StringField(required=True)
    price = db.FloatField(required=True)

    @staticmethod
    def createProduct(body):
        try:
            product = Product.from_json(json.dumps(body), True)
            product.save()
        except Exception as error:
            print(error)

        return product

    @staticmethod
    def getProduct(id):
        try:
            product = Product.objects().get(id=str(id))
            print(product.id)
            data = {}
            data["id"] = str(product.id)
            data["name"] = product.name
            data["stock"] = product.stock
            data["picture"] = product.picture
            data["price"] = product.price



        except Exception as error:
            print(error)

        return data

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
                data["picture"] = product.picture
                data["price"] = product.price

                listProducts.append(data)
            
        except Exception as error:
            print(error)

        return listProducts

    @staticmethod
    def updateProduct(id, body):
        try:
            product = Product.objects().get(id=id).update(name=body["name"])
            product = Product.objects().get(id=id).update(stock=body["stock"])
            product = Product.objects().get(id=id).update(picture=body["picture"])
            product = Product.objects().get(id=id).update(price=body["price"])
            print(product)
            # product.save()
            
        except Exception as error:
            print(error)

        return product

    @staticmethod
    def deleteProduct(id):
        try:
            product = Product.objects().get(id=str(id))
            product.delete()
            
        except Exception as error:
            product = None
            print(error)

        return product