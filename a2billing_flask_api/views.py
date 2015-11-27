from auth import auth
from app import app
from flask import jsonify
from api import user_auth
from peewee import *
# from flask.ext.security import *
from functools import wraps
from flask import g, request, redirect, url_for, Response
# from flask_peewee.rest import RestAPI, UserAuthentication, RestResource
from flask_peewee.rest import Authentication


def response_auth_failed():
    return Response('Authentication failed', 401, {
        'WWW-Authenticate': 'Basic realm="Login Required"'
    })


def custom_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        basic_auth = request.authorization
        if not basic_auth:
            return response_auth_failed()
        g.user = auth.authenticate(basic_auth.username, basic_auth.password)
        if not g.user:
            return response_auth_failed()

        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def homepage():
    return 'Welcome to A2B Restful API!'


@app.route('/private/')
@auth.login_required
def private_view():
    # user = auth.get_logged_in_user()
    return 'This is private!'


# user_auth = UserAuthentication(auth, protected_methods=['GET', 'POST', 'PUT', 'DELETE'])


# @user_auth.auth.login_required
@app.route('/custom_api/refill/<int:card_id>', methods=['POST'])
@custom_login_required
def refill(card_id):
    # show the post with the given id, the id is an integer
    # return 'Card %d' % card_id
    myid = 10
    # prepare dictionary for JSON return
    data = {
        'card_id': card_id,
        'status': 'OK',
        'myid': myid
    }
    return jsonify(data)
