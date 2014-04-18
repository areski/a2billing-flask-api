

DEPLOY A2BILLING-FLASK-API
==========================

There is many ways to deploy a Flask application, here we will focus on deploying on
Apache2 webserver using mod_wsgi. This should be the most easier way for A2Billing
users without installing too many applications on their server.


Installing mod_wsgi
-------------------

If you don’t have mod_wsgi installed yet you have to either install it using a package
manager or compile it yourself.

If you are using Ubuntu/Debian you can apt-get it and activate it as follows:

    # apt-get install libapache2-mod-wsgi


WSGI Application
----------------

To run your application you need an app.wsgi file. Mod_wsgi is executing this
file on startup to get the application object.

The a2billing_flask_app.wsgi is located at the root of this repository.


Configuring Apache
------------------

The last thing you have to do is to create an Apache configuration file for your application.

    <VirtualHost *>
        ServerName example.com

        WSGIDaemonProcess a2billing_flask_app user=user1 group=group1 threads=5
        WSGIScriptAlias / /usr/share/a2billing-flask-api/a2billing_flask_app.wsgi

        <Directory /usr/share/a2billing-flask-api>
            WSGIProcessGroup a2billing_flask_app
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
    </VirtualHost>






