from flask_peewee.auth import Auth
from app import app, db


# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)
