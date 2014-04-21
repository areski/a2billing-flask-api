A2Billing-Flask-API
===================

A2Billing Restful APIs in Flask.


Each Rest Resource exposed via the API supports the following:

    /api/<model name>/ – GET and POST requests

    /api/<model name>/<primary key>/ – GET, PUT and DELETE requests

Also, you can filter results by columns on the model. For example:

    /api/cardgroup/?name=Some%20Blog


Admin Panel
~~~~~~~~~~~

An Admin Panel is provided which can be accessed at http://<ip_address>:8008/admin/

You will need an admin username and password to login, see the section below on how to create an admin user.

View resources

.. image:: https://github.com/areski/a2billing-flask-api/raw/master/screenshots/A2Billing-API-Admin.png

Edit resources

.. image:: https://github.com/areski/a2billing-flask-api/raw/master/screenshots/A2Billing-API-Admin-Edit.png



List of APIs
------------

This is the list of Restful APIs supported.

CardGroup - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of card-groups, create new card-group, Update/Delete existing card-group.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/cardgroup/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/cardgroup/?name=DEFAULT'

    GET ONE: curl -u username:password http://localhost:8008/api/cardgroup/1

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/cardgroup/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:8008/api/cardgroup/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:8008/api/cardgroup/3/


Card - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of cardss, create new card, Update/Delete existing card.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/card/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/card/?username=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/card/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/card/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:8008/api/card/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:8008/api/card/3/


Usage API - Card Group
----------------------

Card Group allows to regroup Card per entity and define agents associated to them, as well as user permissions when accessing
the Customer UI.


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


Usage API - Card
----------------

Cards are A2Billing Users on the A2Billing Platform, this regroups credentials and specific information related to
the users, such as names, address, balance, etc..


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


Requirements
------------

This Application is build using Flask and Peewee:

    * Python 2.5 or greater

    * Flask : http://flask.pocoo.org/

    * Peewee : http://peewee.readthedocs.org/en/latest/

    * Gunicorn : http://gunicorn.org/

    * WTForms : http://wtforms.readthedocs.org/en/latest/

    * MySQL-python : MySQL-python

    * Flask-HTTPAuth : https://pypi.python.org/pypi/Flask-HTTPAuth


Stress Test
-----------

Use ab, the Apache HTTP server benchmarking tool

Usage:

    ab -c 100 -n 1000 -p test/post.txt -T application/x-www-form-urlencoded http://localhost:8008/api/cardgroup/


Install & Deployment
--------------------

There are many ways to deploy a Flask Application, we will describe the Apache Method here as this is the one
more suitable for A2Billing users.


Reference: https://www.digitalocean.com/community/articles/how-to-deploy-a-flask-application-on-an-ubuntu-vps


Security
~~~~~~~~

Edit a2billing_flaskapi.py and change the secret key and keep this really secret:

    app.secret_key = 'ssshhhh-and-changeme-when-deploying'


Create an Admin User
~~~~~~~~~~~~~~~~~~~~

We now have a functioning admin site! Of course, we’ll need a user to log in with,
so open up an interactive python shell in the directory alongside the app and run the following:

$ workon a2billing-flask-api
$ cd /usr/share/a2billing-flask-api/
$ python

Then in Python interpreter, type the following:

    from a2billing_flask_api import auth
    auth.User.create_table(fail_silently=True)  # make sure table created.
    admin = auth.User(username='admin', email='', admin=True, active=True)
    admin.set_password('admin')
    admin.save()


Coding Conventions
------------------

This project is PEP8 compilant and please refer to these sources for the Coding
Conventions : http://www.python.org/dev/peps/pep-0008/


Additional information
-----------------------

License : MPL V2.0

Fork the project on GitHub : https://github.com/areski/a2billing-flask-api

The initial Author is Arezqui Belaid <areski@gmail.com>
