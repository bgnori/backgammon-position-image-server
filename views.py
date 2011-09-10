from werkzeug import Response

import model 
from imageexceptions import *
from imageresponse import FileResponse

def tests(request):
  print 'tests:loading  file tests.html'
  return FileResponse('tests.html', 'text/html', 200)

def list_errors(request):
  f = open('list_errors.html')
  b = f.read()
  f.close()
  return Response(b, mimetype='text/html')

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
  #return FileResponse("failsnake.jpg", mimetype="image/jpeg", status=500)

def not_implemented(request):
  raise NotImplemented()





def image(request):
  '''
    /image?gnubgid=ZrsFAFju3QECCA%3AAgEAAAAAAAAA&height=450&width=600&css=deutsche&format=png

  '''

  img = model.image(
    request.args.get('gnubgid'),
    request.args.get('css'),
    request.args.get('format'),
    int(request.args.get('width')),
    int(request.args.get('height')),
  )

  mimetype = {
    'jpeg':'image/jpeg',
    'png':'image/png',
    'gif':'image/gif',
  }[request.args.get('format')]

  return Response(img, mimetype=mimetype)
  

def gnubg(request):
  '''
    /gnubg?pid= ZrsFAFju3QECCA&mid=AgEAAAAAAAAA&height=450&width=600&css=deutsche&format=png

  '''

  gnubgid = request.args.get('pid')+':'+request.args.get('mid')

  img = model.image(
    gnubgid,
    request.args.get('css'),
    request.args.get('format'),
    int(request.args.get('width')),
    int(request.args.get('height')),
  )

  mimetype = {
    'jpeg':'image/jpeg',
    'png':'image/png',
    'gif':'image/gif',
  }[request.args.get('format')]

  return Response(img, mimetype=mimetype)

def xgid(request):
  '''
    /xgid?xgid=-b-BBBD-----bC---c-dbBb---%3A0%3A0%3A1%3A00%3A0%3A0%3A0%3A5%3A10%0D%0A

    (urlencoded XGID=-b-BBBD-----bC---c-dbBb---:0:0:1:00:0:0:0:5:10)
  '''

  img = model.byxgid(
    request.args.get('xgid'),
    request.args.get('css'),
    request.args.get('format'),
    int(request.args.get('width')),
    int(request.args.get('height')),
  )

  mimetype = {
    'jpeg':'image/jpeg',
    'png':'image/png',
    'gif':'image/gif',
  }[request.args.get('format')]

  return Response(img, mimetype=mimetype)





