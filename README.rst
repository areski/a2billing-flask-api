A2Billing-Flask-API
===================

A2Billing Restful APIs in Flask.


List of APIs
~~~~~~~~~~~~

This is the list of Restful APIs supported:

    Card : Method [GET/POST/PUT/DELETE]

        Get list of card, create new card, Update existing card and




Requirements
------------

This Application is build using Flask and Gevent :

* Flask : http://flask.pocoo.org/



Usage
-----

You can find documentation about the API provided by accessing :
http://0.0.0.0:5000/v1.0/documentation

API Send SMS - http://127.0.0.1:5000/v1.0/sendsms

Parameters::

    @ recipient : Phone Number of the person receving the SMS
    @ message : Message content to be send on the SMS
    @ interface : Set the interface to use to send the SMS, default b0"


Test with CURL::

    curl --dump-header -X POST --data 'recipient=650234300&message="Hello and welcome to my world!&interface=b0' http://0.0.0.0:5000/v1.0/sendsms

    or without interface,

    curl --dump-header -X POST --data 'recipient=650234300&message="Hello' http://0.0.0.0:5000/v1.0/sendsms


Stress Test
-----------

Use ab, the Apache HTTP server benchmarking tool

Usage::

    ab -c 100 -n 1000 -p test/post.txt -T application/x-www-form-urlencoded http://0.0.0.0:5000/v1.0/sendsms


Deployment
----------

There is many ways to deploy a Flask Application, we will describe the Apache Method here as this is the ones
more suitable for A2Billing users.


Reference::

    https://www.digitalocean.com/community/articles/how-to-deploy-a-flask-application-on-an-ubuntu-vps



Create an Admin User
--------------------

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
Conventions :

    - http://www.python.org/dev/peps/pep-0008/


Additional information
-----------------------

License : MIT

Fork the project on GitHub : https://github.com/areski/a2billing-flask-api

The initial Author is Arezqui Belaid <areski@gmail.com>
