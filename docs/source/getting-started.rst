
.. _getting_started:

Getting Started
===============

:Source: https://github.com/areski/a2billing-flask-api/
:Keywords: a2billing, api, flask


Flexible & Fast Restful APIs framework for A2Billing powered by Flask_ & Peewee_.
A2Billing-Flask-API comes with some tools for exposing your A2Billing
models via a RESTful API.

.. _Flask: http://flask.pocoo.org/
.. _Peewee: http://peewee.readthedocs.org/en/latest/


Each RestFul APIs exposed supports the following:

    /api/<model name>/ – GET and POST requests

    /api/<model name>/<primary key>/ – GET, PUT and DELETE requests

Also, you can filter results by columns on the model. For example:

    /api/cardgroup/?name=Some%20Blog


.._admin-panel:

Admin Panel
-----------

An Admin Panel is provided which can be accessed at http://<ip_address>:8008/admin/

You will need an admin username and password to login, see the section below on how to create an admin user.

View resources:

.. image:: https://github.com/areski/a2billing-flask-api/raw/master/screenshots/A2Billing-API-Admin.png

Edit resources:

.. image:: https://github.com/areski/a2billing-flask-api/raw/master/screenshots/A2Billing-API-Admin-Edit.png



.. _requirements:

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


See the file requirements.txt for the full list of requirements.


.. _stress-test:

Stress Test
-----------

Use ab, the Apache HTTP server benchmarking tool

Usage::

    ab -c 100 -n 1000 -p test/post.txt -T application/x-www-form-urlencoded http://localhost:8008/api/cardgroup/


.. _install-deployment:

Install & Deployment
--------------------

There are many ways to deploy a Flask Application, we will describe the Apache Method here as this is the one
more suitable for A2Billing users.


Reference: https://www.digitalocean.com/community/articles/how-to-deploy-a-flask-application-on-an-ubuntu-vps


.. _security:

Security
--------

Edit a2billing_flaskapi.py and change the secret key and keep this really secret::

    app.secret_key = 'ssshhhh-and-changeme-when-deploying'


.. _create-an-admin-user:

Create an Admin User
--------------------

We now have a functioning admin site, you can login with user / password: admin / admin

**Change immediately the default password by a strong password!!!**

You might want to create an other admin user from shell, to do so open up an
interactive python shell in the directory alongside the app and run the following::

    $ cd /usr/share/a2billing-flask-api/
    $ workon a2billing-flask-api
    $ python

Then in Python interpreter, type the following::

    from a2billing_flask_api import auth
    auth.User.create_table(fail_silently=True)  # make sure table created.
    admin = auth.User(username='admin', email='', admin=True, active=True)
    admin.set_password('admin')
    admin.save()
