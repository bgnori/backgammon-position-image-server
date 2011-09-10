
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

