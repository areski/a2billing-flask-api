import datetime
from flask import Flask
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI, UserAuthentication
from peewee import *


# TODO:
# 1. Build proper UI for card
# 2. API working with Documentation for Usage
# 3. Fake data
# 4. Deployment scripts
# 5. Documentation
# 5.1. Add Screenshot to Documentation
#


# configure our database
DATABASE = {
    'name': 'a2billing_db',
    'engine': 'peewee.MySQLDatabase',
    'user': 'root',
    'passwd': 'password',
}

DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper
db = Database(app)


class Card(db.Model):
    # user = ForeignKeyField(User, related_name='tweets')
    creationdate = DateTimeField(default=datetime.datetime.now)
    firstusedate = CharField(null=True)
    expirationdate = CharField(null=True)
    enableexpire = CharField(null=True)
    expiredays = CharField(null=True)
    username = CharField()
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
    initialbalance = DecimalField(default=0)
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
    discount = DecimalField(default=0)
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


# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)

# instantiate the user auth
user_auth = UserAuthentication(auth)
# create a RestAPI container
api = RestAPI(app, default_auth=user_auth)

# register the Note model
api.register(Card, auth=user_auth)
# api.register(User, UserResource, auth=admin_auth)
api.setup()


admin = Admin(app, auth)
admin.register(Card, CardAdmin)
auth.register_admin(admin)
admin.setup()


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    # Note.create_table(fail_silently=True)

    # app.debug = True
    # app.run(host='0.0.0.0', port=PORT)
    app.run()
