from werkzeug import Response

def index(request):
  return Response("Hello, world!", mimetype="text/plain")



