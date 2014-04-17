A2Billing-Flask-API
===================

A2Billing Restful APIs in Flask.


Each Rest Resource exposed via the API supports, the following:

    /api/<model name>/ – GET and POST requests

    /api/<model name>/<primary key>/ – GET, PUT and DELETE requests

Also, you can filter results by columns on the model, for example:

    /api/cardgroup/?name=Some%20Blog


List of APIs
------------

This is the list of Restful APIs supported.

CardGroup - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of card-group, create new card-group, Update/Delete existing card-group.

METHODS:

    GET ALL: curl -u admin:admin http://localhost:5000/api/cardgroup/

    GET ALL FILTER: curl -u admin:admin 'http://localhost:5000/api/cardgroup/?name=DEFAULT'

    GET ONE: curl -u admin:admin http://localhost:5000/api/cardgroup/1

    DELETE: curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:5000/api/cardgroup/4/

    ADD: curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:5000/api/cardgroup/

    UPDATE: curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:5000/api/cardgroup/3/


Card - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of card, create new card, Update/Delete existing card.

METHODS:

    GET ALL: curl -u admin:admin http://localhost:5000/api/card/

    GET ALL FILTER: curl -u admin:admin 'http://localhost:5000/api/card/?username=1321546'

    GET ONE: curl -u admin:admin http://localhost:5000/api/card/1/

    DELETE: curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:5000/api/card/4/

    ADD: curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:5000/api/card/

    UPDATE: curl -u admin:admin --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:5000/api/card/3/


Usage API - Card Group
----------------------

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


Requirements
------------

This Application is build using Flask and Peewee:

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

    ab -c 100 -n 1000 -p test/post.txt -T application/x-www-form-urlencoded http://localhost:5000/api/cardgroup/


Install & Deployment
--------------------

There is many ways to deploy a Flask Application, we will describe the Apache Method here as this is the ones
more suitable for A2Billing users.


Reference: https://www.digitalocean.com/community/articles/how-to-deploy-a-flask-application-on-an-ubuntu-vps


Security
~~~~~~~~

Edit a2billing_flaskapi.py and change the secret key:

    # set the secret key.  keep this really secret:
    app.secret_key = 'ssshhhh-and-changeme-when-deploying'


Create an Admin User
~~~~~~~~~~~~~~~~~~~~

We now have a functioning admin site! Of course, we’ll need a user log in with,
so open up an interactive python shell in the directory alongside the app and run the following:

    > from app import auth
    > auth.User.create_table(fail_silently=True)  # make sure table created.
    > admin = auth.User(username='admin', email='', admin=True, active=True)
    > admin.set_password('admin')
    > admin.save()


Coding Conventions
------------------

This project is PEP8 compilant and please refer to these sources for the Coding
Conventions : http://www.python.org/dev/peps/pep-0008/


Additional information
-----------------------

License : MIT

Fork the project on GitHub : https://github.com/areski/a2billing-flask-api

The initial Author is Arezqui Belaid <areski@gmail.com>
