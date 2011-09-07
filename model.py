import StringIO

import bglib.model
import bglib.model.board
import bglib.encoding.gnubgid
import bglib.encoding.xgid
from bglib.model import constants


import bglib.image.PIL
import bglib.image.resource
import bglib.image.resource.minimal
import bglib.image.resource.safari
import bglib.image.resource.kotobuki
import bglib.image.resource.nature
import bglib.image.resource.flower
import bglib.image.resource.neon
import bglib.image.resource.deutsche


def byxgid(xgid, css, format, width, height):
  b = bglib.model.boardeditor.BoardEditor()
  bglib.encoding.xgid.decode(b, xgid)
  b.flip()

  d = get_draw(css)
  p = get_painter(format)
  return p(b, d, width, height)

def image(gnubgid, css, format, width, height):
  b = bglib.model.boardeditor.BoardEditor()
  bglib.encoding.gnubgid.decode(b, gnubgid[:14], gnubgid[15:27])
  b.flip()

  d = get_draw(css)
  p = get_painter(format)
  return p(b, d, width, height)

def get_draw(css):
  if css == "minimal":
    return bglib.image.PIL.Draw(bglib.image.resource.minimal.css)
  elif css == "safari":
    return bglib.image.PIL.Draw(bglib.image.resource.safari.css)
  elif css == "kotobuki":
    return bglib.image.PIL.Draw(bglib.image.resource.kotobuki.css)
  elif css == "nature":
    return bglib.image.PIL.Draw(bglib.image.resource.nature.css)
  elif css == "flower":
    return bglib.image.PIL.Draw(bglib.image.resource.flower.css)
  elif css == "neon":
    return bglib.image.PIL.Draw(bglib.image.resource.neon.css)
  elif css == "deutsche":
    return bglib.image.PIL.Draw(bglib.image.resource.deutsche.css)
  else:
    assert False

def get_painter(format):
  return {"jpeg":jpeg, "png":png, "gif":gif87a}[format]


def jpeg(b, draw, width, height):
  buf = StringIO.StringIO()
  image = draw.draw(b, (width, height))
  assert image.mode == 'RGBA'
  image.save(buf, 'jpeg')
  return buf.getvalue()

def png(b, draw, width, height):
  buf = StringIO.StringIO()
  image = draw.draw(b, (width, height))
  assert image.mode == 'RGBA'
  image.save(buf, 'png')
  return buf.getvalue()

def gif87a(b, draw, width, height):
  buf = StringIO.StringIO()
  image = draw.draw(b, (width, height))
  assert image.mode == 'RGBA'
  image.save(buf, 'gif')
  return buf.getvalue()


