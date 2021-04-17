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

            invoice.client = client
            invoice.products = products
            # invoice.validate()
            invoice.save()

        except Exception as error:
            print(error)
            invoice = None

        return invoice
