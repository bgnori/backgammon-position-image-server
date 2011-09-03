from werkzeug import Request, ClosingIterator
from werkzeug.exceptions import HTTPException, InternalServerError, NotFound


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
    except NotFound, e:
      response = views.not_found(request)
      #response = views.internal_server_error(request)
    except HTTPException, e:
      response = e
    except:
      '''5xx'''
      response =  views.internal_server_error(request)

    return ClosingIterator(response(environ, start_response), self._cleanup)

  def _setup(self):
    pass
      
  def _cleanup(self):
    pass


