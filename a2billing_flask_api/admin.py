from flask_peewee.admin import Admin, ModelAdmin
from app import app
from auth import auth
from models import CardGroup, Card, Callerid


class CardAdmin(ModelAdmin):
    columns = ('username', 'creationdate',)


class CardGroupAdmin(ModelAdmin):
    columns = ('id', 'name',)


class CalleridAdmin(ModelAdmin):
    columns = ('id', 'id_cc_card', 'activated', 'cid',)


admin = Admin(app, auth, branding='A2Billing API Admin Site')
admin.register(Card, CardAdmin)
admin.register(CardGroup, CardGroupAdmin)
admin.register(Callerid, CalleridAdmin)
auth.register_admin(admin)
