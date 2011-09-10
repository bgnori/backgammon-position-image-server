import StringIO
import os
import re


from werkzeug import Response


import Image
import ImageDraw
import ImageFont

from tonic.cache import memoize, hub
from tonic.cache.imp import *

from mime import is_binary

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


