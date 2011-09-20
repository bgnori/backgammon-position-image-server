.. image-server documentation master file, created by
   sphinx-quickstart on Thu Sep 15 09:03:03 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to image-server's documentation!
========================================

Contents:
This server provides on-the-fly backgammon position image generation.

.. toctree::
   :maxdepth: 2

/image
======
 Some versons of gnubg give ids in format of gnubgid=[pid]:[mid].
This service supports this format. URL encode [pid]&:[mid] part.

i.e. If you have: ::

  sGsQMDWYuxkDQA:cInxAAAAAAAA

then encode it into: ::

  sGsQMDWYuxkDQA%3AcInxAAAAAAAA

and construct uri with other parameters,::

  <img src="/image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png">

and it gives you image of:

   ..  image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png


/gnubg
======
another versions of gnubg give ids in position id and match id in separate form.

i.e. If you have : ::

  Position ID: zN6CATDYzsEBMA
  Match ID: cIl1ABAAAAAA

then urlencode them: ::
  
  zN6CATDYzsEBMA
  cIl1ABAAAAAA

finnaly::

  <img src="/gnubg?pid=zN6CATDYzsEBMA&mid=cIl1ABAAAAAA&width=300&height=200&css=nature&format=png">

and it gives you image of:

  .. image:: ../gnubg?pid=zN6CATDYzsEBMA&mid=cIl1ABAAAAAA&width=300&height=200&css=nature&format=png



/xgid
=====
This feature is experimental.

Here is an XGID::

  XGID=--ABBBBBA------------acCf-:1:1:1:00:4:8:0:11:10

encode part after XGID=::

  --ABBBBBA------------acCf-%3A1%3A1%3A1%3A00%3A4%3A8%3A0%3A11%3A10

construct URL with it.::

  <img src="/xgid?xgid=--ABBBBBA------------acCf-%3A1%3A1%3A1%3A00%3A4%3A8%3A0%3A11%3A10&width=300&height=200&css=nature&format=png">

and it gives you:

  .. image:: ../xgid?xgid=--ABBBBBA------------acCf-%3A1%3A1%3A1%3A00%3A4%3A8%3A0%3A11%3A10&width=300&height=200&css=nature&format=png


Here more samples.
 * XGID=-ACBaBB--BBa-------bcbAcc-:0:0:1:21:0:0:0:1:10

  .. image:: ../xgid?xgid=-ACBaBB--BBa-------bcbAcc-%3A0%3A0%3A1%3A21%3A0%3A0%3A0%3A1%3A10&width=300&height=200&css=nature&format=png

 * XGID=-a-CCBBB--a-a----c-bbC-cb-:0:0:1:52:0:0:0:1:10

  .. image:: ../xgid?xgid=-a-CCBBB--a-a----c-bbC-cb-%3A0%3A0%3A1%3A52%3A0%3A0%3A0%3A1%3A10&width=300&height=200&css=nature&format=png

 * XGID=-a-BBBB-Bb--dC---a-dBc----:0:0:1:66:0:0:0:1:10
  .. image:: ../xgid?xgid=-a-BBBB-Bb--dC---a-dBc----%3A0%3A0%3A1%3A66%3A0%3A0%3A0%3A1%3A10&width=300&height=200&css=nature&format=png

Make sure Encode the id value.

 * XGID=-baaBbCCB-B-aB---bacb----A:0:0:1:43:0:0:0:7:10, (without url encoding)::

   <img src="/xgid?XGID=-baaBbCCB-B-aB---bacb----A:0:0:1:43:0:0:0:7:10&width=300&height=200&css=nature&format=png"/> 

   gives: 

   .. image:: ../xgid?XGID=-baaBbCCB-B-aB---bacb----A:0:0:1:43:0:0:0:7:10&width=300&height=200&css=nature&format=png

Common Parameters
=================

width and height
----------------
width value specifis width of the response image
height value specifis height of the response image
Both values must be with in range of 50 - 1000.
Beware of fitting, aspect ratio over 2 or under .5 may give poor out put.

 * 200x300

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png

 * 400x600

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=600&height=600&css=nature&format=png

 * 200x600
  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=600&height=200&css=nature&format=png




css
---
specifies style for image. 
Currelnty availble are: 'minimal', 'safari','kotobuki',  'nature',
 'flower', 'neon', 'deutsche'

 *  minimal

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=minimal&format=png

 * safari

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=safari&format=png

 * kotobuki

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=kotobuki&format=png

 * natue 

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png

 * flower

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=flower&format=png

 * neon

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=neon&format=png

 * deutsche  

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=deutsche&format=png


format
------
image server support three formats currently. Which are: jpeg, png, and gif.

 * png (recommended)

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png


 * jpeg (not recommended, due to noise)

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=jpeg

 * gif (not recommended, due to noise)

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=gif

HTTP Status Code and Response
=============================

400
---
  400 Bad Request

 .. image:: ../errors/400

When parameters are not specified or baddly specified, it reports error details:

 * broken param

  .. image:: ../image?gnubgid=sGsQMDWYuxA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png

 * bad data
  * bad position id

  .. image:: ../image?gnubgid=s11QMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png

  * bad match id
  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png

  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3A1InxAAAAA111&width=300&height=200&css=nature&format=png

 
 * no width
  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&height=200&css=nature&format=png

 * no height
  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&css=nature&format=png

 * no css
  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&format=png

 * no format
  .. image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature

 * not urlencoded
  .. image:: ../xgid?XGID=-baaBbCCB-B-aB---bacb----A:0:0:1:43:0:0:0:7:10&width=300&height=200&css=nature&format=png

401
---
  401 Unauthorized

 .. image:: .. /errors/401

404
---
  404 Not Found

 .. image:: ../errors/404

405
---
  405 Method Not Allowed

 .. image:: ../errors/405

406
---
  406 Not Acceptable

 .. image:: ../errors/406

408
---
  408 Request Timeout (result depends on browser)

 .. image:: ../errors/408

412
---
  412 Precondition Failed

 .. image:: ../errors/412

413
---
  413 Request Entity Too Large

 .. image:: ../errors/413

414
---
  414 Request-URI Too Long

 .. image:: ../errors/414

415
---
  415 Unsupported Media Type

 .. image:: ../errors/415

417
---
  417 Expectation Failed

 .. image:: ../errors/417

418
---
  418 I'm a teapot 

 .. image:: ../errors/418

500
---
  500 Internal Server Error

 .. image:: ../errors/500

501
---
  501 Not Implemented

 .. image:: ../errors/501


How to report bugs
==================

Please send mail to bgnori@gmail.com, with:

 * subject of "bug at image.backgammonbase.com". 

 * your request, i.e. http://image.backgammonbase.com/... etc.

 * describe the phenomenon you got.


About
=====

Copyright 2011 Noriyuki Hosaka(bgnori@gmail.com)

Commercial Use: Need to pay me. please contact with above address.
No charge for non-comercial use or during development/domestic use.
If you are making above 1000requests/hr, Please contact. 
