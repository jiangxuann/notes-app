from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://xuan:tbAb1h4Dgcx98njY@cluster0.6lx36jd.mongodb.net/?retryWrites=true&w=majority"

mongo = PyMongo(app)
db = mongo.cx["test_database"]

from application import routes