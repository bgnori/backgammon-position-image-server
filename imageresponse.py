import StringIO
import os

from werkzeug import Response
from werkzeug import security


import Image
import ImageDraw
import ImageFont

from tonic.cache import memoize, hub
from tonic.cache.imp import *

from mime import is_binary, guess_mimetype

hub.connect(Dict())


@memoize(hub)
def load_file_as(fname, mtime, option, mimetype):
  f = open(fname, option)
  b = f.read()
  #FIXME content negotiation.
  f.close()
  return b
  

def FileResponse(fname, mimetype, status):
  if is_binary(mimetype):
    option = 'rb'
  else:
    option = 'r'
  
  mtime = os.stat(fname).st_mtime

  b = load_file_as(fname, mtime, option, mimetype)
  return Response(b, mimetype=mimetype, status=status)


def DocumentRoot(root, path, status):
  safe = security.safe_join(root, path)
  print '"%s" + "%s" ==> "%s"'%(root, path  ,safe)

  mime = guess_mimetype(path)
  mtime = os.stat(safe).st_mtime
  return FileResponse(safe, mime, status)

