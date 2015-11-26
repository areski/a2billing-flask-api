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


class CardGroup(db.Model):
    name = CharField()
    description = TextField(null=True)
    users_perms = IntegerField(default=0)
    id_agent = IntegerField(default=0)

    class Meta:
        db_table = 'cc_card_group'


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
