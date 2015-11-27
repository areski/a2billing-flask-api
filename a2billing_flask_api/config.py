# config


class Configuration(object):
    # Configure your A2Billing database
    DATABASE = {
        'name': 'a2billing_db',
        'engine': 'peewee.MySQLDatabase',
        'user': 'root',
        'passwd': 'password',
    }
    DEBUG = True
    # Set the secret key.  keep this really secret
    # Default implementation stores all session data in a signed cookie. This requires that the secret_key is set
    SECRET_KEY = 'THE_SECRET_KEY'
