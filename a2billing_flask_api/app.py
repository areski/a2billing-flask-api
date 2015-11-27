from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')
# app.config.from_object(__name__)

# Instantiate the db wrapper
db = Database(app)
