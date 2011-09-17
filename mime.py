import re


image_mime_types = {
  'image/jpeg': 'jpeg',
  'image/png' : 'png', 
  'image/gif' : 'gif'
}


def mime2fext(mimetype):
  ret = image_mime_types[mimetype]
  assert ret
  return ret

binaries = re.compile('image/')
def is_binary(mimetype):
  return  bool(binaries.match(mimetype))


cap = {
  #'ttf': 'ttf',
  'css': 'text/css',
  'html': 'text/html',
  'png': "image/png",
  'js': "text/javascript",
}

def guess_mimetype(path):
  print path
  trunk, ext = path.rsplit(".")
  try:
    return cap[ext]
  except KeyError:
    return 'application/octet-stream'
