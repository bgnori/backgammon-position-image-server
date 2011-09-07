#!/usr/bin/python
# utf8


from werkzeug.debug import DebuggedApplication
from wsgiref.util import setup_testing_defaults
from werkzeug.serving import run_simple
#from wsgiref.simple_server import make_server

from app import Application

def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    return ret

wz_test = Application()
wz_test = DebuggedApplication(wz_test)
run_simple('127.0.0.1', 8000, wz_test, use_debugger=True, use_reloader=True)


