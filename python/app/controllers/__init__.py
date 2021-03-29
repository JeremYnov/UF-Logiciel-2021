from app.controllers.ClientController import ClientController

def routes(api):
    api.add_resource(ClientController, '/api/clients', '/api/client/<string:id>', '/api/client/<string:id>/update', '/api/client/new')
