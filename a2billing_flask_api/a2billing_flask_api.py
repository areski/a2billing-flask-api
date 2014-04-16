#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

from gevent.event import Event
from gevent.wsgi import WSGIServer
from flask import Flask, request, abort
from werkzeug.utils import escape
from time import sleep
import ESL
from singleton import singleton

import sys
import logging
import optparse
from daemon import Daemon
from werkzeug.exceptions import BadRequest, InternalServerError

import redis
from random import randint
from uuid import uuid1
import re

__version__ = 'v1.0'

PORT = 5000

#Event Socket
EVENTSOCKET_HOST = '127.0.0.1'
EVENTSOCKET_PORT = '8021'
EVENTSOCKET_PASSWORD = 'ClueCon'

TESTDEBUG = False

# List of interface of Khomp Card
#INTERFACE_LIST = ['*b0', '*b1', '*b2', '*b3']
INTERFACE_LIST = ['*b0']
# Number of SIM cards on the Khomp Card
N_SIM = 4
#Expire Ressource / 300 seconds
SIM_TTL = 10
#Ressouce name
RESNAME = 'interface'

r_server = redis.Redis(host='localhost', port=6379)


def interface_reserve(sinterface=None):
    """This function will try to find an interface we can use to send SMS
    which hasn't been busy for the last SIM_TTL
    it will select randomly an interface and then will increment to find
    one that is available.
    """
    #Get Random SIM
    randsim = randint(1, N_SIM)

    if sinterface:
        #Search on a Specific Interface
        for i in range(1, N_SIM + 1):
            nextsim = (randsim + i) % N_SIM + 1
            mkey = "%s-%s-%d" % (RESNAME,
                        sinterface,
                        nextsim)
            if not r_server.get(mkey):
                #Reserve ressource
                r_server.set(mkey, 1)
                r_server.expire(mkey, SIM_TTL)
                return mkey
    else:
        #Get random interface
        randinterf = randint(0, len(INTERFACE_LIST) - 1)

        for j in range(len(INTERFACE_LIST)):
            nextinterf = (randinterf + j) % len(INTERFACE_LIST)
            for i in range(1, N_SIM + 1):
                nextsim = (randsim + i) % N_SIM + 1
                mkey = "%s-%s-%d" % (RESNAME,
                            INTERFACE_LIST[nextinterf],
                            nextsim)
                if not r_server.get(mkey):
                    #reserve ressource
                    r_server.set(mkey, 1)
                    r_server.expire(mkey, SIM_TTL)
                    return mkey
                #else:
                    #Ressource busy
                    #print "Ressource Busy"
    return False


# for k in range(1, 20):
#     res_interface = interface_reserve()
#     #res_interface = interface_reserve('b0')
#     print res_interface
# sys.exit()

@singleton
class connectESL(object):
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.con = ESL.ESLconnection(self.host, self.port, self.password)

    def spam_connection(self):
        return self.con

    def reconnect(self):
        self.con = ESL.ESLconnection(self.host, self.port, self.password)

handler_esl = connectESL(
    EVENTSOCKET_HOST,
    EVENTSOCKET_PORT,
    EVENTSOCKET_PASSWORD)

app = Flask(__name__)

#setup logger
logger = logging.getLogger("sms_khomp_api")
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler("/var/log/sms-khomp-api/sms_khomp_api.log")
fh.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s [%(levelname)s] "
    "%(name)s\t%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)


# see https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/exceptions.py
class MyBadRequest(BadRequest):
    def get_body(self, environ):
        return (
            'ERR: %(name)s %(description)s %(code)s'
        ) % {
            'code': self.code,
            'name': escape(self.name),
            'description': self.get_description(environ)
        }


class MyInternalServerError(InternalServerError):
    def get_body(self, environ):
        return (
            'ERR: %(name)s %(description)s %(code)s'
        ) % {
            'code': self.code,
            'name': escape(self.name),
            'description': self.get_description(environ)
        }

abort.mapping.update({400: MyBadRequest})
abort.mapping.update({500: MyInternalServerError})


#Add Flask Routes
@app.route("/")
def index():
    return "Welcome to Khomp SMS API " + __version__


@app.route("/documentation/")
def documenation():
    documentation = "<b>DOCUMENTATION</b><br>"\
        "------------------------------<br/>"\
        "<br/>Send SMS - Url <b>/v1.0/sendsms</b><br/><br/>"\
        "Parameters :<br/>"\
        " @ recipient : Phone Number of the person receving the SMS<br>"\
        " @ message : Message content to be send on the SMS<br/>"\
        " @ interface : Set the interface to use to send the SMS, default b0"
    return documentation

#@app.route('/v1.0/sendsms/<recipient>/<sender>/<message>')
#def sendsms(recipient, sender, message):
#    # show the user profile for that user
#    return 'Send SMS %s / %s / %s' % (recipient, sender, message)


@app.route('/v1.0/sendsms', methods=['POST'])
def sendsms():
    if request.method == 'POST':
        if 'recipient' in request.form \
           and 'message' in request.form:

            if 'interface' in request.form \
               and len(request.form['interface']) > 1:
                #Get interface
                interface = request.form['interface']
            else:
                interface = None

            recipient = request.form['recipient']
            message = request.form['message']

            if (TESTDEBUG):
                #reserve a ressource
                rsd_int = interface_reserve(interface)
                if not rsd_int:
                    #TODO: Check 500 code, replace something for throttle
                    abort(500, 'ERR: Ressource unvailable throttle')

                interface = rsd_int.split('-')[1]
                logger.info("Ressource is being used %s - %s" %
                    (rsd_int, interface))
                sleep(0.001)

                #Prepare SMS command
                command_string = "sms %s %s '%s'" % \
                    (str(interface), str(recipient), str(message))
                logger.info(command_string)

                #Send SMS Via Khomp FreeSWITCH API
                #...

                #Free ressource
                r_server.delete(rsd_int)
                return "ID: %s Mock SMS Success 200" % str(uuid1())
            else:
                #reserve a ressource
                rsd_int = interface_reserve(interface)
                if not rsd_int:
                    #TODO: Check 500 code, replace something for throttle
                    logger.error("ERR: Ressource unvailable throttle")
                    abort(500, 'ERR: Ressource unvailable throttle')

                interface = rsd_int.split('-')[1]
                logger.info("Ressource is being used %s - %s" %
                    (rsd_int, interface))

                if not handler_esl.con.connected():
                    #Try to reconnect
                    handler_esl.reconnect()
                    if not handler_esl.con.connected():
                        r_server.delete(rsd_int)
                        abort(500, 'ERR: Cannot connect to FreeSWITCH')

                #Prepare SMS command
                command_string = "concise sms %s %s '%s'" % \
                    (str(interface), str(recipient), str(message))

                try:
                    #Send SMS via Khomp API
                    ev = handler_esl.con.api("khomp", command_string)
                    #Retrieve result
                    result = ev.getBody()
                    logger.info(result)
                except AttributeError:
                    #Free ressource
                    r_server.delete(rsd_int)
                    abort(500, 'ID: %s (Internal Error Get Result) 501')

                #Free ressource
                r_server.delete(rsd_int)

                #Parse result code
                if result.find('OK') > 0:
                    return "ID: %s (Success) 200" % str(uuid1())
                else:
                    try:
                        m = re.search('-*\d+', result)
                        err_code = m.group(0)
                    except:
                        err_code = '502'
                    try:
                        m = re.search('\(.+\)', result)
                        err_message = m.group(0)
                    except:
                        err_message = '(Internal Error Parse Err)'
                    return "ID: %s %s %s" % (
                        str(uuid1()),
                        err_message,
                        err_code)

            #return 'Received POST ==> Send SMS %s / %s / %s' % \
            #        (request.form['recipient'], request.form['message'],
            #        request.form['interface'])
        else:
            if not 'recipient' in request.form:
                abort(404, 'ERR: Missing parameter "recipient" on POST')
            if not 'message' in request.form:
                abort(404, 'ERR: Missing parameter "message" on POST')
            if not 'interface' in request.form:
                abort(404, 'ERR: Missing parameter "interface" on POST')
            abort(404, 'ERR: Missing parameters on POST')
    else:
        return 'OK: Send recipient, sender and message via POST'


class StdErrWrapper:
    def __init__(self):
        self.logger = logging.getLogger("sms_khomp_api.access")

    def write(self, s):
        self.logger.info(s.rstrip())


class MyDaemon(Daemon):
    def run(self):
        #while True:
        self.logger = logging.getLogger("sms_khomp_api")
        self.logger.info("Creating sms_khomp_api")
        #Run WSGIServer
        http = WSGIServer(('', PORT), app.wsgi_app)
        http.serve_forever()
        self.logger.info("Done.")


if __name__ == "__main__":
    parser = optparse.OptionParser(usage="usage: %prog -d|c|m|e [options]",
                    version="SMS Khomp API Server " + __version__)
    parser.add_option("-c", "--config", action="store", dest="config",
                    default="configfile.cfg", help="Path to config file",)
    parser.add_option("-d", "--daemon", action="store_true", dest="daemon",
                    default=False, help="Start as daemon",)
    parser.add_option("-e", "--debug", action="store_true", dest="debug",
                    default=False, help="Start in debug mode",)
    parser.add_option("-m", "--master", action="store_true", dest="master",
                    default=False, help="Start master in foreground",)
    parser.add_option("-p", "--pid", action="store", dest="pid",
                    default="/tmp/sms_khomp_api.pid", help="Path to pid file",)

    (options, args) = parser.parse_args()
    if options.daemon:
        daemon = MyDaemon(options.pid)

        if len(args) != 1:
            parser.error("Missing parameters : "
                "sms_khomp_api.py -d start|stop|restart")

        if "start" == args[0]:
            daemon.start()
        elif "stop" == args[0]:
            daemon.stop()
        elif "restart" == args[0]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)

    elif options.master:
        print "Starting as master (PORT:%d)..." % PORT
        daemon = MyDaemon(options.pid)
        #daemon.load_config(options.config)
        try:
            daemon.run()
        except KeyboardInterrupt:
            print "\nGot Ctrl-C, shutting down..."
        except Exception, e:
            print "Oops...", e
        print "Bye!"

    elif options.debug:
        print "Starting in debug mode (PORT:%d)..." % PORT
        app.debug = True
        app.run(host='0.0.0.0', port=PORT)

    else:
        parser.print_usage()
        sys.exit(1)
