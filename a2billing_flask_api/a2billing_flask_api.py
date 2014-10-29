import datetime
from flask import Flask
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI, UserAuthentication, RestResource
# from flask import Blueprint, abort, request, Response, session, redirect, url_for, g
from flask import request
import json
from peewee import *

# Configure your A2Billing database
DATABASE = {
    'name': 'a2billing_db',
    'engine': 'peewee.MySQLDatabase',
    'user': 'root',
    'passwd': 'password',
}

app = Flask(__name__)
app.config.from_object(__name__)

# Set the secret key.  keep this really secret
# Default implementation stores all session data in a signed cookie. This requires that the secret_key is set
app.secret_key = 'THE_SECRET_KEY'

# Instantiate the db wrapper
db = Database(app)


@app.route('/')
def homepage():
    return 'Welcome to A2B Restful API!'

"""
Usage API - Card Group
----------------------

GET ALL
~~~~~~~

$ curl -u username:password http://localhost:8008/api/cardgroup/

    {
      "meta": {
        "model": "cardgroup",
        "next": "",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "id_agent": null,
          "description": "This group is the default group used when you create a customer. It's forbidden to delete it because you need at least one group but you can edit it.",
          "users_perms": 262142,
          "id": 1,
          "name": "DEFAULT"
        },
        {
          "id_agent": 0,
          "description": null,
          "users_perms": 0,
          "id": 2,
          "name": "NewGroup"
        }
      ]
    }

GET ONE
~~~~~~~

$ curl -u username:password http://localhost:8008/api/cardgroup/1/

    {
      "id_agent": null,
      "description": "This group is the default group used when you create a customer. It's forbidden to delete it because you need at least one group but you can edit it.",
      "users_perms": 262142,
      "id": 1,
      "name": "DEFAULT"
    }

DELETE
~~~~~~

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/cardgroup/4/

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 18
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 16:11:03 GMT

    {
      "deleted": 1
    }

ADD
~~~

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:8008/api/cardgroup/

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 96
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 16:08:55 GMT

    {
      "id_agent": 0,
      "description": "",
      "users_perms": 0,
      "id": 3,
      "name": "mygroup"
    }

UPDATE
~~~~~~

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:8008/api/cardgroup/3/

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 104
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 16:12:31 GMT

    {
      "id_agent": 0,
      "description": "",
      "users_perms": 0,
      "id": 3,
      "name": "mygroup-updated"
    }
"""


class CardGroup(db.Model):
    name = CharField()
    description = TextField(null=True)
    users_perms = IntegerField(default=0)
    id_agent = IntegerField(default=0)

    class Meta:
        db_table = 'cc_card_group'


"""
Usage API - Card
----------------

GET ALL
~~~~~~~

$ curl -u username:password http://localhost:8008/api/card/
    {
      "meta": {
        "model": "card",
        "next": "",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "email_notification": "areski@gmail.com",
          "status": 1,
          "expiredays": null,
          "loginkey": "4654",
          "lock_pin": "0",
          "useralias": "312224525577965",
          "uipass": "18314euvyzix7spr1eew",
          "activated": "f",
          "currency": "USD",
          "tag": "ok",
          "initialbalance": 0.0,
          "voicemail_activated": 0,
          ...
          ...

GET ONE
~~~~~~~

$ curl -u username:password http://localhost:8008/api/card/1/
    {
      "email_notification": "areski@gmail.com",
      "status": 1,
      "expiredays": null,
      "loginkey": "4654",
      "lock_pin": "0",
      "useralias": "312224525577965",
      "uipass": "18314euvyzix7spr1eew",
      "activated": "f",
      "currency": "USD",
      "tag": "ok",
      "initialbalance": 0.0,
      "voicemail_activated": 0,
      "redial": "0",
      "id": 1,
      "sip_buddy": 1,
      "city": "Barcelona",
      "id_group": 1,
      ...
      ...

DELETE
~~~~~~

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/card/4/

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 18
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 18:50:43 GMT

    {
      "deleted": 1
    }

ADD
~~~

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"username": "1234567890", "useralias": "0554654648", "lastname": "Belaid", "firstname": "Areski", "uipass": "6546456", "credit": "5", "tariff": "1"}' http://localhost:8008/api/card/

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 1257
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 23:33:14 GMT

    {
      "email_notification": "",
      "status": 1,
      "expiredays": null,
      "loginkey": "",
      "lock_pin": null,
      "useralias": "0554654648",
      "uipass": "6546456",
      "activated": null,
      "currency": "USD",
      "tag": "",
      "initialbalance": 0.0,
      "voicemail_activated": 0,
      "redial": "",
      "id": 7,
      "sip_buddy": 0,
      "city": "",
      "id_group": 1,
      "notify_email": 0,
      ...
      ...


UPDATE
~~~~~~

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"lastname": "Belaid"}' http://localhost:8008/api/card/7/

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 1290
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 23:36:10 GMT

    {
      "email_notification": "",
      "status": 1,
      "expiredays": "",
      "loginkey": "",
      "lock_pin": null,
      "useralias": "0554654648",
      "uipass": "6546456",
      "activated": "f",
      "currency": "USD",
      "tag": "",
      "initialbalance": 0.0,
      "voicemail_activated": 0,
      "redial": "",
      "id": 7,
      "sip_buddy": 0,
      "city": "",
      "id_group": 1,
      "notify_email": 0,
      ...
      ...
"""


class Card(db.Model):
    # user = ForeignKeyField(User, related_name='tweets')
    creationdate = DateTimeField(default=datetime.datetime.now)
    firstusedate = CharField(null=True)
    expirationdate = CharField(null=True)
    enableexpire = CharField(null=True)
    expiredays = CharField(null=True)
    username = CharField(null=False)
    useralias = CharField()
    uipass = CharField()
    credit = CharField()
    tariff = CharField()
    id_didgroup = CharField(null=True)
    activated = CharField(choices=(('f', 'False'), ('t', 'True')))
    status = IntegerField(default=1)
    lastname = CharField(default='')
    firstname = CharField(default='')
    address = CharField(default='')
    city = CharField(default='')
    state = CharField(default='')
    country = CharField(default='')
    zipcode = CharField(default='')
    phone = CharField(default='')
    email = CharField(default='')
    fax = CharField(default='')
    # inuse = CharField(null=True)
    simultaccess = IntegerField(default=0)
    currency = CharField(default='USD')
    # lastuse = CharField(null=True)
    # nbused = CharField(null=True)
    typepaid = IntegerField(default=0)
    creditlimit = IntegerField(default=0)
    voipcall = IntegerField(default=0)
    sip_buddy = IntegerField(default=0)
    iax_buddy = IntegerField(default=0)
    language = CharField(default='en')
    redial = CharField(default='')
    runservice = CharField(null=True)
    # nbservice = CharField(null=True)
    # id_campaign = CharField(null=True)
    # num_trials_done = CharField(null=True)
    vat = FloatField(null=False, default=0)
    # servicelastrun = CharField(null=True)
    # Using DecimalField produce an error
    initialbalance = FloatField(default=0.0)
    invoiceday = IntegerField(default=1)
    autorefill = IntegerField(default=0)
    loginkey = CharField(default='')
    mac_addr = CharField(default='00-00-00-00-00-00')
    id_timezone = IntegerField(default=0)
    tag = CharField(default='')
    voicemail_permitted = IntegerField(default=0)
    voicemail_activated = IntegerField(default=0)
    # last_notification = CharField(null=True)
    email_notification = CharField(default='')
    notify_email = IntegerField(default=0)
    credit_notification = IntegerField(default=-1)
    id_group = IntegerField(default=1)
    company_name = CharField(default='')
    company_website = CharField(default='')
    vat_rn = CharField(null=True)
    traffic = BigIntegerField(default=0)
    traffic_target = CharField(default='')
    # Using DecimalField produce an error
    discount = FloatField(default=0.0)
    # restriction = CharField(null=True)
    # id_seria = CharField(null=True)
    # serial = CharField(null=True)
    block = IntegerField(default=0)
    lock_pin = CharField(null=True)
    lock_date = DateTimeField(null=True)
    max_concurrent = IntegerField(default=10)
    # is_published = BooleanField(default=True)

    class Meta:
        db_table = 'cc_card'


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
    app.run()
