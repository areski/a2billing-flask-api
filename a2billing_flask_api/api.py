from flask_peewee.rest import RestAPI, UserAuthentication, RestResource
from flask import request
from auth import auth
from app import app
from models import CardGroup, Card, Callerid, Logrefill, Call, Country
# from models import Did, DidDestination
import json


# create a special resource for users that excludes email and password
class CardResource(RestResource):
    # exclude = ('lock_pin',)

    def check_post(self):
        datajson = json.loads(request.data)
        if 'username' not in datajson or len(datajson['username']) == 0:
            return False
        if 'useralias' not in datajson or len(datajson['useralias']) == 0:
            return False
        if 'uipass' not in datajson or len(datajson['uipass']) == 0:
            return False
        if 'credit' not in datajson or len(datajson['credit']) == 0:
            return False
        if 'tariff' not in datajson or len(datajson['tariff']) == 0:
            return False

        return True


# create a special resource for users that excludes email and password
class UserResource(RestResource):
    exclude = ('password', 'email',)


# class LogrefillResource(RestResource):

#     def prepare_data(self, obj, data):
#         data["credit"] = str(data["credit"])
#         return data


# instantiate the user auth
user_auth = UserAuthentication(auth, protected_methods=['GET', 'POST', 'PUT', 'DELETE'])


# create a RestAPI container
api = RestAPI(app, default_auth=user_auth)
# register the models
api.register(Card, CardResource, auth=user_auth)
api.register(CardGroup, auth=user_auth)
api.register(Callerid, auth=user_auth)
api.register(Logrefill, auth=user_auth)
api.register(Call, auth=user_auth)
api.register(Country, auth=user_auth)
# api.register(Did, auth=user_auth)
# api.register(DidDestination, auth=user_auth)
api.register(auth.User, UserResource, auth=user_auth)
