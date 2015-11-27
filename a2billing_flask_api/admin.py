from flask_peewee.admin import Admin, ModelAdmin
from app import app
from auth import auth
from models import CardGroup, Card


class CardAdmin(ModelAdmin):
    columns = ('username', 'creationdate',)


class CardGroupAdmin(ModelAdmin):
    columns = ('id', 'name',)


admin = Admin(app, auth, branding='A2Billing API Admin Site')
admin.register(Card, CardAdmin)
admin.register(CardGroup, CardGroupAdmin)
auth.register_admin(admin)
