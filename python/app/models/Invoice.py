import json

from datetime import datetime

from app.models import db
from app.models.Product import Product
from app.models.Client import Client

class Invoice(db.Document):
    meta = {'collection': 'Invoice'}
    client = db.ReferenceField(Client)
    issueDate = db.DateTimeField(default=datetime.now())
    isPaid = db.BooleanField(default=False)
    paymentDate = db.DateTimeField()
    price = db.FloatField(default=0.0)
    products = db.ListField(db.ReferenceField(Product))


    @staticmethod
    def create(body):
        try:
            invoice = Invoice()

            client = Client.objects.get(id=body['client'])

            products = []

            for productId in body['products']:
                product = Product.objects.get(id=productId)
                invoice.price += product.price
                products.append(product)

            invoice.price = round(invoice.price, 2)
            invoice.client = client
            invoice.products = products
            # invoice.validate()
            invoice.save()

        except Exception as error:
            print(error)
            invoice = None

        return invoice
    
    @staticmethod
    def getAllInvoice():
        try:
            invoices = Invoice.objects().all()
            listInvoice = []
            for invoice in invoices :
                data = {}
                data["id"] = str(invoice.id)
                
                data["issueDate"] = invoice.issueDate
                data["isPaid"] = invoice.isPaid
                data["paymentDate"] = invoice.paymentDate
                data["price"] = invoice.price
                data["products"] = []
                
                dataClient = {}
                dataClient['id'] = str(invoice.client.id)
                dataClient['firstName'] = invoice.client.firstName
                dataClient['lastName'] = invoice.client.lastName
                dataClient['email'] = invoice.client.email
                dataClient['creation'] = invoice.client.creation.strftime('%d/%m/%Y')
                data["client"] = dataClient
                
                for product in invoice.products :
                    dataProduct = {}
                    dataProduct["id"] = str(product.id)
                    dataProduct["name"] = product.name
                    dataProduct["stock"] = product.stock
                    dataProduct["price"] = product.price
                    dataProduct["image"] = {}
                    dataProduct["image"]["url"] = f"/api/product/{str(product.id)}/image/{product.picture.filename}"
                    dataProduct["image"]["name"] = product.picture.filename
                    data["products"].append(dataProduct) 
                    
                listInvoice.append(data)
            
        except Exception as error:
            print(error)

        return listInvoice

    @staticmethod
    def getInvoice(id):
        try:
            invoice = Invoice.objects().get(id=id)
            data = {}
            data["id"] = str(invoice.id)
            data["issueDate"] = invoice.issueDate
            data["isPaid"] = invoice.isPaid
            data["paymentDate"] = invoice.paymentDate
            data["price"] = invoice.price
            data["products"] = []
            
            dataClient = {}
            dataClient['id'] = str(invoice.client.id)
            dataClient['firstName'] = invoice.client.firstName
            dataClient['lastName'] = invoice.client.lastName
            dataClient['email'] = invoice.client.email
            dataClient['creation'] = invoice.client.creation.strftime('%d/%m/%Y')
            data["client"] = dataClient
            
            for product in invoice.products :
                dataProduct = {}
                dataProduct["id"] = str(product.id)
                dataProduct["name"] = product.name
                dataProduct["stock"] = product.stock
                dataProduct["price"] = product.price
                dataProduct["image"] = {}
                dataProduct["image"]["url"] = f"/api/product/{str(product.id)}/image/{product.picture.filename}"
                dataProduct["image"]["name"] = product.picture.filename
                data["products"].append(dataProduct) 

        except Exception as error:
            print(error)

        return data

    @staticmethod
    def deleteInvoice(id):
        try:
            invoice = Invoice.objects().get(id=id)
            invoice.delete()
            
        except Exception as error:
            invoice = None
            print(error)

        return invoice
    
    @staticmethod
    def update(id, body):
        try:
            updated = {
                "count": 0
            }

            invoice = Invoice.objects().get(id=id)
            if body["client"]:
                client = Client.objects.get(id=body['client'])
                invoice.client = client
                updated["client"] = "updated"
                updated["count"] += 1
            
            print(type(body["isPaid"]))
            if body["isPaid"] == True:
                invoice.isPaid = body["isPaid"]
                invoice.paymentDate = datetime.now()
                updated["isPaid"] = "updated"
                updated["count"] += 1
            if body["isPaid"] == False :
                invoice.isPaid = body["isPaid"]
                invoice.paymentDate = None
                updated["isPaid"] = "updated"
                updated["count"] += 1
            
            if body["products"]:
                products = []
                invoice.price = 0
                for productId in body['products']:
                    product = Product.objects.get(id=productId)
                    invoice.price += product.price
                    products.append(product)
                invoice.products = products
                updated["products"] = "updated"
                updated["count"] += 1
            
            invoice.save()

        except Exception as error:
            print(error)

        return updated

    @staticmethod
    def isClientDelete(client):
        if not Invoice.objects(client=client["id"]) :
            return True

        return False

    @staticmethod
    def isProductDelete(product):
        if not Invoice.objects(products__contains=str(product['id'])) :
            return True

        return False
