import os
import sys


activate_this = '/usr/share/virtualenvs/a2billing-flask-api/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))


apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path.insert(0, '/usr/share/virtualenvs/a2billing-flask-api/lib/python2.6/site-packages')
sys.path.insert(1, '/usr/share/virtualenvs/a2billing-flask-api/lib/python2.7/site-packages')
sys.path.append('/usr/share')
sys.path.append('/usr/share/a2billing-flask-api')

# os.environ['DJANGO_SETTINGS_MODULE'] = 'newfies_dialer.settings'
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()

from a2billing_flask_api import app as application
