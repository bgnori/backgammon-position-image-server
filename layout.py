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
    self.size = size
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

  def fold(self, box):
    self.fold_CRLF(box)

  def fold_CRLF(self, box):
    print 'fold_CRLF "%s"'%(box.text,)
    lines = box.text.splitlines()
    for line in lines:
      p = box.get_param()
      b = self.make_box(p, line)
      if self.is_X_overflaw(b):
        self.fold_WHITE(b)
      else:
        self.push(b)

  def fold_WHITE(self, box):
    print 'fold_WHITE "%s"'%(box.text,)
    last = 0
    line = box.text
    end = len(line)
    p = box.get_param()
    for n, c in enumerate(line):
      if c not in ' \t\v\n' and n < end:
        pass
      else:
        b = self.make_box(p, text=line[:n])
        print 'trying %3d "%s"'%(n, b.text,)
        if not self.is_X_overflaw(b):
          last = n
          continue
        else:
          if last == 0:
            #no way to fold. give up
            print 'no way to fold. give up'
            self.push(box)
            return
          else:
            break

    b = self.make_box(p, line)
    if not self.is_X_overflaw(b):
      print 'no need to fold.'
      self.push(b)
      return 

    b = self.make_box(p, line[:last])
    self.push(b)
    rest = line[last:] 
    rest = rest.strip()
    if rest:
      print 'rest: "%s"'%(rest,)
      box = self.make_box(p, rest)
      self.fold_WHITE(box)


  def push(self, box):
    print 'push "%s"'%(box.text,)
    rect = box.get_rect()
    self.boxes.append(box)
    self.current[1] = rect[1][1]
    
  def pop(self):
    assert self.boxes
    box = self.boxes.pop()
    if self.boxes:
      last = self.boxes[-1]
      rect = last.get_rect()
      self.current[1] = rect[1][1]
    else:
      self.current[1] = 0
    return box
    
  def make_box(self, arg, text=None):
    arg.update({'topleft': tuple(self.current)})
    if text:
      arg.update({'text': text})
    return Box(**arg)

  def is_X_overflaw(self, box):
    rect = box.get_rect()
    return rect[1][0] > self.size[0]

  def add(self, name, **arg):
    print 'add"%s"'%(arg['text'],)
    assert name == 'text'
    box = self.make_box(arg)

    if not self.is_X_overflaw(box):
      self.push(box)
    else:
      self.fold(box)

  def render(self):
    for box in self.boxes:
      box.render(self)



class Model(object):
  def __init__(self, padding):
    assert len(padding) == 2
    self.padding = padding

  def get_param(self):
    d = {}
    d.update(self.__dict__)
    return d

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


