from werkzeug import Request, ClosingIterator
from werkzeug.exceptions import HTTPException


from urls import url_map

import views



class Application(object):
  def __init__(self):
    pass
  
  def __call__(self, environ, start_response):
    try:
      self._setup()
      request = Request(environ)
      adapter = url_map.bind_to_environ(environ)
      endpoint, values = adapter.match()
      handler = getattr(views, endpoint)
      response = handler(request, **values)

    except HTTPException, e:
      '''5xx'''
      return ClosingIterator(e(environ, start_response), self._cleanup)

    return ClosingIterator(response(environ, start_response), self._cleanup)

  def _setup(self):
    pass
      
  def _cleanup(self):
    pass


