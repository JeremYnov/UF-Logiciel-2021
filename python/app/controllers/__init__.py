from app.controllers.ClientController import ClientController

def routes(api):
    api.add_resource(ClientController, '/api/client/<int:id>/update', '/api/client/new')
