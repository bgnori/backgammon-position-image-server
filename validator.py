from exceptions import ValueError

from decorator import decorator

from imageexceptions import BadRequest


def method(acceptables):
  def entangle(f):
    def method(func, request):
      if request.method in acceptables:
        return func(request)
      else:
        return views.method_not_allowed(request)
    return decorator(method, func)
  return entangle

def isInt(x):
  try:
    p = int(x, 10)
  except (ValueError, TypeError):
    return False
  return True

def intRange(name, r, default=None):
  def entangle(func):
    def intRange(func, request):
      rmin, rmax = r
      v = request.args.get(name, default)
      msg = ('Need %s value within range of %d - %d')%(name, rmin, rmax)
      print name, v, isInt(v), v < rmin, v > rmax
      if not v or not isInt(v) or int(v) < rmin or int(v) > rmax:
        return BadRequest(msg)
      return func(request)
    return decorator(intRange, func)
  return entangle

def oneOf(name, cs, default=None):
  def entangle(func):
    def oneOf(func, request):
      v = request.args.get(name, default)
      msg = ('Need %s value one of %s')%(name, cs)
      if not v or not v in cs:
        return BadRequest(msg)
      return func(request)
    return decorator(oneOf, func)
  return entangle


def stringLength(name, n, hint=None):
  def entangle(func):
    def stringLength(func, request):
      v = request.args.get(name, '')
      #print 'stringLength: "%s"'%(v,)
      msg = ('Need %s value be %d long')%(name, n)
      if hint:
        msg += hint
      if not v or not len(v) == n :
        return BadRequest(msg)
      return func(request)
    return decorator(stringLength, func)
  return entangle


