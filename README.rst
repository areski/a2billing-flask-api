A2Billing-Flask-API
===================

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


Documentation
-------------

A2Billing-Flask-API's documentation can be found at http://a2billing-flask-api.readthedocs.org/en/latest/index.html


Coding Conventions
------------------

This project is PEP8 compilant and please refer to these sources for the Coding
Conventions : http://www.python.org/dev/peps/pep-0008/


Additional information
-----------------------

License: MPL V2.0

Fork the project on GitHub: https://github.com/areski/a2billing-flask-api

The initial Author is Arezqui Belaid <areski@gmail.com>
