#!/usr/bin/python
# utf8


from werkzeug.debug import DebuggedApplication
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

from app import Application

def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    return ret

#httpd = make_server('', 8000, simple_app)
wz_test = Application()
wz_test = DebuggedApplication(wz_test)

httpd = make_server('', 8000, wz_test)
print "Serving on port 8000..."
httpd.serve_forever()

