import re
from werkzeug.wrappers import BaseResponse
from werkzeug.exceptions import HTTPException
from werkzeug._internal import _get_environ
from werkzeug.utils import escape
from werkzeug import exceptions


from mime import mime2fext
from layout import Render


DEFAULT_IMAGE_SIZE = (400, 200)
#DEFAULT_IMAGE_SIZE = (1200, 400)
WperH_RATIO_RANGE = (0.5, 4.0)

to_remove = re.compile(r'<p>')
to_split = re.compile(r'</p>')
def html2lines(html):
  for t in to_split.split(to_remove.sub('', html)):
    yield t

class ImageMixin(object):
  def get_mimetype(self, environ):
    #FIXME add content negotiation
    return "image/jpeg"
  
  def get_detail(self, environ):
    '''get detail of error'''
    return self.detail
  
  #def get_description(self, environ):

  def get_body(self, environ):
    r = Render(DEFAULT_IMAGE_SIZE)
    mimetype = self.get_mimetype(environ)

    r.Box(("%(code)s: %(name)s"
        ) % {
            'code':         self.code,
            'name':         escape(self.name),
        },
        (5, 5),
        "DejaVuLGCSans-Bold.ttf", 16)

    for line in html2lines(self.get_description(environ)):
      r.Box(line, (3, 3), "DejaVuLGCSans-Bold.ttf", 10)

    return r.render(mimetype)

  def rewritten_headers(self, environ):
    
    headers = self.get_headers(environ)
    # invoke HTTPException derived class method.
    
    r = []
    """Get a list of headers."""
    # do some replace.
    # [('Content-Type', 'text/html')] => [('Content-Type', 'image/???')]
    for h, v in headers:
      if h == 'Content-Type':
        r.append(('Content-Type', self.get_mimetype(environ)))
      else:
        r.append(h, v)
    return r

  def get_response(self, environ):
      environ = _get_environ(environ) #UGH!
      headers = self.rewritten_headers(environ)
      return BaseResponse(self.get_body(environ), self.code, headers)



class BadRequest(ImageMixin, exceptions.BadRequest):
  pass

class Unauthorized(ImageMixin, exceptions.Unauthorized):
  pass

class Forbidden(ImageMixin, exceptions.Forbidden):
  pass

class NotFound(ImageMixin, exceptions.NotFound):
  pass

class MethodNotAllowed(ImageMixin, exceptions.MethodNotAllowed):
  pass

class NotAcceptable(ImageMixin, exceptions.NotAcceptable):
  pass

class RequestTimeout(ImageMixin, exceptions.RequestTimeout):
  pass

class Conflict(ImageMixin, exceptions.Conflict):
  pass

class Gone(ImageMixin, exceptions.Gone):
  pass

class LengthRequired(ImageMixin, exceptions.LengthRequired):
  pass

class PreconditionFailed(ImageMixin, exceptions.PreconditionFailed):
  pass

class RequestEntityTooLarge(ImageMixin, exceptions.RequestEntityTooLarge):
  pass

class RequestURITooLarge(ImageMixin, exceptions.RequestURITooLarge):
  pass

class UnsupportedMediaType(ImageMixin, exceptions.UnsupportedMediaType):
  pass

class RequestedRangeNotSatisfiable(ImageMixin, exceptions.RequestedRangeNotSatisfiable):
  pass

class ExpectationFailed(ImageMixin, exceptions.ExpectationFailed):
  pass

class ImATeapot(ImageMixin, exceptions.ImATeapot):
  pass

class InternalServerError(ImageMixin, exceptions.InternalServerError):
  pass

class NotImplemented(ImageMixin, exceptions.NotImplemented):
  pass

class BadGateway(ImageMixin, exceptions.BadGateway):
  pass

class ServiceUnavailable(ImageMixin, exceptions.ServiceUnavailable):
  pass







