import StringIO

import Image
import ImageDraw
import ImageFont

from tonic.cache import memoize, hub
from tonic.cache.imp import *

from mime import mime2fext

@memoize(hub)
def calc_font_size(font_name, size, text):
  #fsize = size[1]

  fsize = 20
  font = load_font(font_name, fsize)
  w, h = font.getsize(text)
  while w >= size[0] or h >= size[1]:
    fsize = fsize - 1
    if fsize < 8: # FIXME
      return None, w, h
    font = load_font(font_name, fsize)
    w, h = font.getsize(text)
  return fsize, w, h


def add(*xys):
  return tuple(map(sum, zip(*xys)))


class DC(object):
  def __init__(self, size):
    self.img = Image.new('RGBA', size)
    self.draw = ImageDraw.Draw(self.img)
    self.boxes = []
    self.current = [0, 0]
  
  @memoize(hub)
  def load_font(self, uri, size):
    assert uri
    font = ImageFont.truetype(uri, size)
    return font

  def getvalue(self, mimetype):
    buf = StringIO.StringIO()
    self.img.save(buf, mime2fext(mimetype))
    return buf.getvalue()

  def add(self, name, **arg):
    print 'dc:add'
    assert name == 'text'
    arg.update({'topleft': tuple(self.current)})
    self.boxes.append(Box(**arg))
    last = self.boxes[-1]
    print last.get_rect()
    self.current[1] = last.get_rect()[1][1]
    print self.current

  def render(self):
    for box in self.boxes:
      box.render(self)



class Model(object):
  def __init__(self, padding):
    assert len(padding) == 2
    self.padding = padding

  def render(self, dc):
    pass

  def get_rect(self):
    pass



class Box(Model):
  def __init__(self, text, topleft, padding, font):
    Model.__init__(self, padding)
    self.topleft = topleft
    self.text = text
    self.font = font

  def getsize(self):
    return self.font.getsize(self.text)

  def get_rect(self):
    ''' tl , br '''
    return (self.topleft, 
          add(self.topleft, 
              self.padding, 
              self.getsize(),
              self.padding))


  def render(self, dc):
    start = add(self.topleft, self.padding)
    dc.draw.text(start, self.text, font=self.font)#, fill='black')


def render(lines, mimetype, size, fsize):

    padding = 10, 10 
    dc = DC(size)

    font_name = 'DejaVuLGCSans-Bold.ttf'
    font = dc.load_font(font_name, fsize)
  
    for line in lines:
      dc.add('text', text=line, padding=padding, font=font)

    dc.render()
    return dc.getvalue(mimetype)


