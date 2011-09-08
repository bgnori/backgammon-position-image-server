from werkzeug import Response

import model 
from imageresponse import FileResponse, DrawTextResponse



def list_errors(request):
  f = open('list_errors.html')
  b = f.read()
  f.close()
  return Response(b, mimetype='text/html')

def bad_request(request):
  return DrawTextResponse("400: Bad Request.", (600, 200), mimetype="image/jpeg", status=400)

def unauthorized(request):
  return DrawTextResponse("401: Unauthorized.", (600, 200), mimetype="image/jpeg", status=401)

def not_found(request):
  return DrawTextResponse("404: No enter found.", (600, 200), mimetype="image/jpeg", status=404)

def method_not_allowed(request):
  return DrawTextResponse("405: Method not allowed.", (600, 200),  mimetype="image/jpeg", status=405)

def not_acceptable(request):
  return DrawTextResponse("406: Not Acceptable.", (600, 200),  mimetype="image/jpeg", status=406)

def request_timeout(request):
  return DrawTextResponse("408: Request timeout.", (600, 200),  mimetype="image/jpeg", status=408)
  
def precondition_failed(request):
  return DrawTextResponse("412: Precondition Failed", (600, 200),  mimetype="image/jpeg", status=412)

def request_entity_too_large(request):
  return DrawTextResponse("413: Request Entity Too Large", (600, 200),  mimetype="image/jpeg", status=413)

def request_uri_too_long(request):
  return DrawTextResponse("414: Requested URI Too Long",  (600, 200), mimetype="image/jpeg", status=414)

def unsupported_media_type(request):
  return DrawTextResponse("415: Unsupported media type", (600, 200),  mimetype="image/jpeg", status=415)

def expectation_failed(request):
  return DrawTextResponse("417: expectation failed.", (600, 200), mimetype="image/jpeg", status=417)

def Im_python(request):
  return DrawTextResponse("418: I'm python.", (600, 200), mimetype="image/jpeg", status=418)

def internal_server_error(request):
  return FileResponse("failsnake.jpg", mimetype="image/jpeg", status=500)

def not_implemented(request):
  return DrawTextResponse("501: No implemented.", (600, 200), mimetype="image/jpeg", status=501)

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





