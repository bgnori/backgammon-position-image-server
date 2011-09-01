import StringIO


from werkzeug import Response


import Image
import ImageDraw
import ImageFont


def get_format(mimetype):
  image_mime_types = {
    'image/jpeg': 'jpeg',
    'image/png' : 'png', 
    'image/gif' : 'gif'
  }
  ret = image_mime_types[mimetype]
  assert ret
  return ret


cache = {}


def FileResponse(fname, mimetype, status):
  f = open(fname, 'rb')
  b = f.read()
  f.close()
  return Response(b, mimetype=mimetype, status=status)


def calc_font_size(font_name, size, text):
  print 'calc_font_size'
  #fsize = size[1]

  fsize = 20
  font = load_font(font_name, fsize)
  w, h = font.getsize(text)
  print 'getsize'
  while w >= size[0] or h >= size[1]:
    fsize = fsize - 1
    if fsize < 8: # FIXME
      return None, w, h
    font = load_font(font_name, fsize)
    w, h = font.getsize(text)
  return fsize, w, h

def load_font(uri, size):
  print "load_font", uri, size
  if (uri, size)  in cache:
    return cache[(uri, size)]
  assert uri
  font = ImageFont.truetype(uri, size)
  cache.update({(uri, size): font})
  return font


def DrawResponse(text, size, mimetype, status=None):
  print 'DrawResponse'
  buf = StringIO.StringIO()
  img = Image.new('RGBA', size)
  draw = ImageDraw.Draw(img)

  print 'context is ready'

  x, y = 10, 10 
  font_name = 'DejaVuLGCSans-Bold.ttf'
  fsize, w, h = calc_font_size(font_name, size, text)
  print fsize,w,h
  if fsize is None: #FIXME
    return

  font = load_font(font_name, fsize)
  xoff = (size[0] - w)/2
  yoff = (size[1] - h)/2

  print font
  print 'offsets', xoff, yoff
  draw.text((x+xoff, y+yoff), text, font=font)#, fill='black')

  print mimetype, '==>', get_format(mimetype)
  img.save(buf, get_format(mimetype))
  
  print 'saved image....'
  b = buf.getvalue()

  return Response(b, mimetype=mimetype, status=status)


