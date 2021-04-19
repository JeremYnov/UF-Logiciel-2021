from app.controllers.ClientController import ClientController
from app.controllers.ProductController import ProductController
from app.controllers.InvoiceController import InvoiceController

def routes(api):
     api.add_resource(ProductController, '/api/product/form', '/api/product/<string:id>/image/<string:filename>', '/api/product/<string:id>/update', '/api/product/new', '/api/product/<string:id>', '/api/products', '/api/product/<string:id>/delete')
     api.add_resource(ClientController, '/api/client/form', '/api/clients', '/api/client/<string:id>', '/api/client/<string:id>/update', '/api/client/<string:id>/delete', '/api/client/new')
     api.add_resource(InvoiceController,  '/api/invoice')
