from werkzeug import Response

import model 
from imageresponse import FileResponse, DrawTextResponse

def index(request):
  return Response("Hello, world!", mimetype="text/plain")


def foofoo(request):
  return DrawResponse("foofoo", (400, 200), mimetype="image/png", status=200)

def not_found(request):
  return DrawTextResponse("404: No enter found.", (600, 200), mimetype="image/jpeg", status=404)


def internal_server_error(request):
  return FileResponse("failsnake.jpg", mimetype="image/jpeg", status=500)

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





