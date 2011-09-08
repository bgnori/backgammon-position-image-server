#!/usr/bin/python
# utf8


from werkzeug.debug import DebuggedApplication
from wsgiref.util import setup_testing_defaults
from werkzeug.serving import run_simple

from app import Application


wz_test = Application()
wz_test = DebuggedApplication(wz_test)
run_simple('127.0.0.1', 8000, wz_test, use_debugger=True, use_reloader=True)


