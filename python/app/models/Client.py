from . import db

class Client(db.Document):
    meta = {'collection': 'Client'}
    firstName = db.StringField(required=True)
    lastName = db.StringField(required=True)

    # def to_json(self):
    #     return {
    #         "firstName": self.firstName,
    #         "lastName": self.lastName
    #     }
