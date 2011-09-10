import StringIO

import Image
import ImageDraw
import ImageFont

from werkzeug.wrappers import BaseResponse
from werkzeug.exceptions import HTTPException
from werkzeug._internal import _get_environ
from werkzeug.utils import escape
from werkzeug import exceptions

from tonic.cache import memoize, hub
from tonic.cache.imp import *

from mime import mime2fext



DEFAULT_IMAGE_SIZE = (600, 200)
#DEFAULT_IMAGE_SIZE = (1200, 400)
WperH_RATIO_RANGE = (0.5, 4.0)


@memoize(hub)
def calc_font_size(font_name, size, text):
  #fsize = size[1]

  fsize = 20
  font = load_font(font_name, fsize)
  w, h = font.getsize(text)
  while w >= size[0] or h >= size[1]:
    fsize = fsize - 1
    if fsize < 8: # FIXME
      return None, w, h
    font = load_font(font_name, fsize)
    w, h = font.getsize(text)
  return fsize, w, h

@memoize(hub)
def load_font(uri, size):
  assert uri
  font = ImageFont.truetype(uri, size)
  return font


class ImageMixin(object):
  def get_mimetype(self, environ):
    #FIXME add content negotiation
    return "image/jpeg"
  
  def get_detail(self, environ):
    '''get detail of error'''
    return self.detail
  
  #def get_description(self, environ):

  def get_body(self, environ):
    mimetype = self.get_mimetype(environ)
    text = ("%(code)s: %(name)s"
    #        "%(description)s\n"
    ) % {
            'code':         self.code,
            'name':         escape(self.name),
    #        'description':  self.get_description(environ)
    }
    buf = StringIO.StringIO()

    size = DEFAULT_IMAGE_SIZE #600, 200) #FIXME
    img = Image.new('RGBA', size)
    draw = ImageDraw.Draw(img)


    x, y = 10, 10 
    font_name = 'DejaVuLGCSans-Bold.ttf'
    fsize, w, h = calc_font_size(font_name, size, text)
    if fsize is None: #FIXME
      return None

    font = load_font(font_name, fsize)
    xoff = (size[0] - w)/2
    yoff = (size[1] - h)/2

    draw.text((x+xoff, y+yoff), text, font=font)#, fill='black')

    img.save(buf, mime2fext(mimetype))
    
    return  buf.getvalue()

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







