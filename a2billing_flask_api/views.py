from auth import auth
from app import app
from flask import jsonify
from peewee import *
from functools import wraps
from flask import g, request, redirect, url_for, Response
from models import Card, Logrefill, Logpayment, Charge
import datetime


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
    return 'This is private!'


@app.route('/custom_api/refill/<int:card_id>', methods=['POST'])
@custom_login_required
def refill(card_id):
    if not request.json or 'credit' not in request.json:
        return Response('Missing credit parameter.', 400)

    # Get Card(vat, credit)
    card = Card.select(Card.credit).where(Card.id == card_id)
    if not card and not card[0]:
        return Response('Card not found.', 400)

    vat = card[0].vat

    credit = float(request.json['credit'])
    prev_credit = card[0].credit
    new_balance = prev_credit + credit
    Card.update(credit=new_balance).where(Card.id == card_id).execute()

    credit_without_vat = credit / (1 + vat / 100)

    # add logrefill
    logrefill = Logrefill(card=card_id, date=datetime.datetime.now, credit=credit, refill_type=0)
    logrefill.save()

    # add logpayment
    logpayment = Logpayment(card=card_id, date=datetime.datetime.now, payment=credit, payment_type=0, id_logrefill=logrefill.id)
    logpayment.save()

    # prepare dictionary for JSON return
    data = {
        'card_id': card_id,
        'current_balance': new_balance,
        'credit_without_vat': credit_without_vat,
        'credited': credit,
        'vat': card[0].vat,
        'logrefill_id': logrefill.id,
        'logpayment_id': logpayment.id
    }
    return jsonify(data)


@app.route('/custom_api/extra_charge/<int:card_id>', methods=['POST'])
@custom_login_required
def extra_charge(card_id):
    if not request.json or 'amount' not in request.json:
        return Response('Missing amount parameter.', 400)

    # Get Card
    card = Card.select(Card.credit).where(Card.id == card_id)
    if not card and not card[0]:
        return Response('Card not found.', 400)

    amount = float(request.json['amount'])
    prev_credit = card[0].credit
    new_balance = prev_credit - amount
    Card.update(credit=new_balance).where(Card.id == card_id).execute()

    # add charge
    charge = Charge(id_cc_card=card_id, amount=amount, chargetype=4)
    charge.save()

    # prepare dictionary for JSON return
    data = {
        'card_id': card_id,
        'current_balance': new_balance,
        'amount': amount,
        'charge_id': charge.id
    }
    return jsonify(data)
