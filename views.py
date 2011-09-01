from werkzeug import Response

from imageresponse import FileResponse, DrawResponse

def index(request):
  return Response("Hello, world!", mimetype="text/plain")


def foofoo(request):
  return DrawResponse("foofoo", (400, 200), mimetype="image/png", status=200)

def not_found(request):
  return DrawResponse("404: No enter found. U are closed out", (400, 200), mimetype="image/jpeg", status=404)


def internal_server_error(request):
  return FileResponse("failsnake.jpg", mimetype="image/jpeg", status=500)


