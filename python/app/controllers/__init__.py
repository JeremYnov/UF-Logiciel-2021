from app.controllers.ClientController import ClientController
from app.controllers.ProductController import ProductController

def routes(api):
     api.add_resource(ClientController, '/api/clients', '/api/client/<string:id>', '/api/client/<string:id>/update', '/api/client/new')
     api.add_resource(ProductController, '/api/product/<string:id>/update', '/api/product/new', '/api/product/<string:id>', '/api/products')
   
