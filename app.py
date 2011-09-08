from werkzeug import Request, ClosingIterator
from werkzeug.exceptions import *


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

      '''4xx'''
    except NotFound:
      response = views.not_found(request)
    except Unauthorized:
      response = views.unauthorized(request)
    except MethodNotAllowed:
      response = views.method_not_allowed(request)
    except NotAcceptable:
      response = views.not_acceptable(request)
    except RequestTimeout:
      response = views.request_timeout(request)
    except PreconditionFailed:
      response = views.precondition_failed(request)
    except RequestEntityTooLarge:
      response = views.request_entity_too_large(request)
    except RequestURITooLarge:
      response = views.request_uri_too_long(request)
    except UnsupportedMediaType:
      response = views.unsupported_media_type(request)
    except ExpectationFailed:
      response = views.expectation_failed(request)
    except IAmTeapot:
      response = views.Im_python(request)
    except BadRequest:
      response = views.bad_request(request)

    except NotImplemented:
      response = views.not_implemented(request)

    except:
      '''5xx'''
      response =  views.internal_server_error(request)

    return ClosingIterator(response(environ, start_response), self._cleanup)

  def _setup(self):
    pass
      
  def _cleanup(self):
    pass


