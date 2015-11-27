from flask_peewee.admin import Admin, ModelAdmin
from app import app
from auth import auth
from models import CardGroup, Card, Callerid, Logrefill


class CardAdmin(ModelAdmin):
    columns = ('username', 'creationdate',)


class CardGroupAdmin(ModelAdmin):
    columns = ('id', 'name',)


class CalleridAdmin(ModelAdmin):
    columns = ('id', 'id_cc_card', 'activated', 'cid',)


class LogrefillAdmin(ModelAdmin):
    columns = ('id', 'card', 'date', 'credit', 'refill_type',)


admin = Admin(app, auth, branding='A2Billing API Admin Site')
admin.register(Card, CardAdmin)
admin.register(CardGroup, CardGroupAdmin)
admin.register(Callerid, CalleridAdmin)
admin.register(Logrefill, LogrefillAdmin)
auth.register_admin(admin)
