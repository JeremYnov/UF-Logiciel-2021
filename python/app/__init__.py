from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .models import db
from .controllers import routes

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# app.config['MONG_DBNAME'] = 'Client'
app.config['DEBUG'] = True
app.config['MONGODB_HOST'] = 'mongodb+srv://dbUser:aBOOwWrdssnBWFty@cluster0.u8qzx.mongodb.net/Api?retryWrites=true&w=majority'

db.init_app(app)
routes(api)
