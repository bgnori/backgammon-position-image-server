import urlparse

from werkzeug import Response

from bglib.encoding import EncodingError as PossibleBadRequest

import model 
from imageexceptions import *
from imageresponse import FileResponse, DocumentRoot

import validator 

def index(request):
  return FileResponse('html/index.html', 'text/html', 200)

def usersguide(request, **kws):
  path = kws.get('path', 'index.html')
  print request.base_url, path
  return DocumentRoot('./doc/build/html/', path, 200)

def addon(request):
  return FileResponse('html/addon.html', 'text/html', 200)

def list_errors(request):
  return FileResponse('html/list_errors.html', 'text/html', 200)

def bad_request(request):
  raise BadRequest()

def unauthorized(request):
  raise Unauthorized()

def not_found(request):
  raise NotFound()

def method_not_allowed(request):
  raise MethodNotAllowed()

def not_acceptable(request):
  raise NotAcceptable()

def request_timeout(request):
  raise RequestTimeout()
  
def precondition_failed(request):
  raise PreconditionFailed()

def request_entity_too_large(request):
  raise RequestEntityTooLarge()

def request_uri_too_long(request):
  raise RequestURITooLarge()

def unsupported_media_type(request):
  raise UnsupportedMediaType()

def expectation_failed(request):
  raise ExpectationFailed()

def Im_python(request):
  raise ImATeapot()

def internal_server_error(request):
  raise InternalServerError()
  #return FileResponse("resource/failsnake.jpg", mimetype="image/jpeg", status=500)

def not_implemented(request):
  raise NotImplemented()



@validator.method(('GET',))
@validator.stringLength('gnubgid', 27)
@validator.oneOf('css', ('minimal', 'safari','kotobuki',  'nature',
 'flower', 'neon', 'deutsche'))
@validator.oneOf('format', ('png', 'jpeg','gif'))
@validator.intRange('width', (50, 1000))
@validator.intRange('height', (50, 1000))
def image(request):
  '''
    /image?gnubgid=ZrsFAFju3QECCA%3AAgEAAAAAAAAA&height=450&width=600&css=deutsche&format=png

  '''

  try:
    img = model.image(
      request.args.get('gnubgid'),
      request.args.get('css'),
      request.args.get('format'),
      int(request.args.get('width')),
      int(request.args.get('height')),
    )
  except PossibleBadRequest, e:
    raise BadRequest(str(e))
  except Exception, e:
    raise InternalServerError(str(e))

  mimetype = {
    'jpeg':'image/jpeg',
    'png':'image/png',
    'gif':'image/gif',
  }[request.args.get('format')]

  return Response(img, mimetype=mimetype)
  

@validator.method(('GET',))
@validator.stringLength('mid', 12)
@validator.stringLength('pid', 14)
@validator.oneOf('css', ('minimal', 'safari','kotobuki',  'nature',
 'flower', 'neon', 'deutsche'))
@validator.oneOf('format', ('png', 'jpeg','gif'))
@validator.intRange('width', (50, 1000))
@validator.intRange('height', (50, 1000))
def gnubg(request):
  '''
    /gnubg?pid= ZrsFAFju3QECCA&mid=AgEAAAAAAAAA&height=450&width=600&css=deutsche&format=png

  '''

  gnubgid = request.args.get('pid')+':'+request.args.get('mid')

  try:
    img = model.image(
      gnubgid,
      request.args.get('css'),
      request.args.get('format'),
      int(request.args.get('width')),
      int(request.args.get('height')),
    )
  except PossibleBadRequest, e:
    raise BadRequest(str(e))
  except Exception, e:
    raise InternalServerError(str(e))

  mimetype = {
    'jpeg':'image/jpeg',
    'png':'image/png',
    'gif':'image/gif',
  }[request.args.get('format')]

  return Response(img, mimetype=mimetype)

@validator.method(('GET',))
@validator.oneOf('css', ('minimal', 'safari','kotobuki',  'nature',
 'flower', 'neon', 'deutsche'))
@validator.oneOf('format', ('png', 'jpeg','gif'))
@validator.intRange('width', (50, 1000))
@validator.intRange('height', (50, 1000))
def xgid(request):
  '''
    /xgid?xgid=-b-BBBD-----bC---c-dbBb---%3A0%3A0%3A1%3A00%3A0%3A0%3A0%3A5%3A10

    (urlencoded XGID=-b-BBBD-----bC---c-dbBb---:0:0:1:00:0:0:0:5:10)
  '''

  try:
    img = model.byxgid(
      request.args.get('xgid'),
      request.args.get('css'),
      request.args.get('format'),
      int(request.args.get('width')),
      int(request.args.get('height')),
    )
  except PossibleBadRequest, e:
    raise BadRequest(str(e))
  except Exception, e:
    raise InternalServerError(str(e))

  mimetype = {
    'jpeg':'image/jpeg',
    'png':'image/png',
    'gif':'image/gif',
  }[request.args.get('format')]

  return Response(img, mimetype=mimetype)





