import datetime
from flask import Flask
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI, UserAuthentication
from peewee import *


# TODO:
# [X] 1. Build proper UI for card
# [X] 2. Build Restful API
# [ ]    2.1. Build Documentation for Restful API
# [X] 3. Fake data
# [ ] 4. Deployment scripts
# [ ] 5. Documentation
# [ ]    5.1. Add Screenshot to Documentation
#


# configure our database
DATABASE = {
    'name': 'a2billing_db',
    'engine': 'peewee.MySQLDatabase',
    'user': 'root',
    'passwd': 'password',
}

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# set the secret key.  keep this really secret
# Default implementation stores all session data in a signed cookie. This requires that the secret_key is set
app.secret_key = 'ssshhhh-and-changeme-when-deploying'

# instantiate the db wrapper
db = Database(app)


"""
API - Card Group
----------------

GET ALL
~~~~~~~

$ curl -u admin:admin http://localhost:5000/api/cardgroup/
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

$ curl -u admin:admin http://localhost:5000/api/cardgroup/1/
{
  "id_agent": null,
  "description": "This group is the default group used when you create a customer. It's forbidden to delete it because you need at least one group but you can edit it.",
  "users_perms": 262142,
  "id": 1,
  "name": "DEFAULT"
}

DELETE
~~~~~~

$ curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:5000/api/cardgroup/4/

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

$ curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:5000/api/cardgroup/

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

$ curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:5000/api/cardgroup/3/
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
API - Card
----------

GET ALL
~~~~~~~

$ curl -u admin:admin http://localhost:5000/api/card/
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

$ curl -u admin:admin http://localhost:5000/api/card/1/
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

$ curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:5000/api/card/4/

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

$ curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X POST --data '{"lastname": "Belaid", "firstname": "Areski"}' http://localhost:5000/api/card/

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
}%

UPDATE
~~~~~~

$ curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:5000/api/card/3/
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


# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)

# instantiate the user auth
user_auth = UserAuthentication(auth, protected_methods=['GET', 'POST', 'PUT', 'DELETE'])
# create a RestAPI container
api = RestAPI(app, default_auth=user_auth)

# register the Note model
api.register(Card, auth=user_auth)
api.register(CardGroup, auth=user_auth)
# api.register(User, UserResource, auth=admin_auth)
api.setup()


admin = Admin(app, auth)
admin.register(Card, CardAdmin)
admin.register(CardGroup, CardGroupAdmin)
auth.register_admin(admin)
admin.setup()


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    # Note.create_table(fail_silently=True)

    app.debug = True
    # app.run(host='0.0.0.0', port=PORT)
    app.run()
