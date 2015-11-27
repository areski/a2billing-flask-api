from flask_peewee.auth import Auth
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI, UserAuthentication, RestResource
from app import app, db
from models import CardGroup, Card
# from flask import Blueprint, abort, request, Response, session, redirect, url_for, g
from flask import request
import json
from peewee import IntegrityError

# from models import *

# from auth import *
# from admin import admin
# from api import api
# from views import *

# admin.setup()
# api.setup()


class CardAdmin(ModelAdmin):
    columns = ('username', 'creationdate',)


class CardGroupAdmin(ModelAdmin):
    columns = ('id', 'name',)


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


# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)

# instantiate the user auth
user_auth = UserAuthentication(auth, protected_methods=['GET', 'POST', 'PUT', 'DELETE'])
# create a RestAPI container
api = RestAPI(app, default_auth=user_auth)
# register the models
api.register(Card, CardResource, auth=user_auth)
api.register(CardGroup, auth=user_auth)
api.register(auth.User, UserResource, auth=user_auth)
api.setup()


admin = Admin(app, auth, branding='A2Billing API Admin Site')
admin.register(Card, CardAdmin)
admin.register(CardGroup, CardGroupAdmin)
auth.register_admin(admin)
admin.setup()


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    # Note.create_table(fail_silently=True)
    try:
        admin = auth.User(username='admin', email='', admin=True, active=True)
        admin.set_password('admin')
        admin.save()
    except IntegrityError:
        print "User 'admin' already created!"

    app.debug = True
    app.run(host='0.0.0.0', port=8008)
