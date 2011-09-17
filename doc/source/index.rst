.. image-server documentation master file, created by
   sphinx-quickstart on Thu Sep 15 09:03:03 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to image-server's documentation!
========================================

Contents:

.. toctree::
   :maxdepth: 2

/image
======
 Some versons of gnubg give ids in format of gnubgid=[pid]:[mid].
This service supports this format. URL encode [pid]&:[mid] part.

i.e. If you have:

  sGsQMDWYuxkDQA:cInxAAAAAAAA

then encode it into:

  sGsQMDWYuxkDQA%3AcInxAAAAAAAA

and construct uri with other parameters,

  <img src="/image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png">

and it gives you image of:

   ..  image:: ../image?gnubgid=sGsQMDWYuxkDQA%3AcInxAAAAAAAA&width=300&height=200&css=nature&format=png


/gnubg
======
another versions of gnubg give ids in position id and match id in separate form.

i.e. If you have :

  Position ID: zN6CATDYzsEBMA
  Match ID: cIl1ABAAAAAA

then urlencode them:
  
  zN6CATDYzsEBMA
  cIl1ABAAAAAA

finnaly

  <img src="/gnubg?pid=zN6CATDYzsEBMA&mid=cIl1ABAAAAAA&width=300&height=200&css=nature&format=png">

and it gives you image of:

  .. image:: ../gnubg?pid=zN6CATDYzsEBMA&mid=cIl1ABAAAAAA&width=300&height=200&css=nature&format=png



/xgid
=====
This feature is experimental.

Here is an XGID

  XGID=--ABBBBBA------------acCf-:1:1:1:00:4:8:0:11:10

encode part after XGID=

  --ABBBBBA------------acCf-%3A1%3A1%3A1%3A00%3A4%3A8%3A0%3A11%3A10

construct URL with it.

  <img src="/xgid?xgid=--ABBBBBA------------acCf-%3A1%3A1%3A1%3A00%3A4%3A8%3A0%3A11%3A10&width=300&height=200&css=nature&format=png">

and it gives you:

  .. image:: ../xgid?xgid=--ABBBBBA------------acCf-%3A1%3A1%3A1%3A00%3A4%3A8%3A0%3A11%3A10&width=300&height=200&css=nature&format=png

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




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

