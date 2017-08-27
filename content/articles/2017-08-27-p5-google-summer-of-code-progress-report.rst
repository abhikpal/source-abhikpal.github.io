p5: Google Summer of Code progress report
=========================================

:date: 2017-08-27 00:21:31 +0100
:tags: python, processing, gsoc, p5
:comments: True

What was the project about?
---------------------------

The main goal of the project was to create a Python library based on
Processing. While Processing's emphasis on teaching programming in a
visual context does make it easier for beginners, the fact that it's
based on Java often makes it look needlessly complex to most
beginners. The main motivation behind creating p5 was to leverage
Python's readability and Processing's emphasis on coding in a visual
context to make programming easier to teach.

The Python mode for Processing was also created for similar reasons,
however, since Python mode was based on Jython, it limited the ways
people could use Python. This was another motivation for creating p5,
we wanted a library that used the Processing API while at the same
time giving people access to Python's large ecosystem of libraries.

Goals for the GSOC
------------------

We wanted to use the GSOC period to mostly create the internal
plumbing required to write basic Processing sketches. In particular,
our initial goals were to:

* Create a system that could work with Processing-style sketches i.e.,
  if the user defines a `mouse_pressed` function, p5 should be able to
  automatically attach an handler to it, if the user defines a `draw`
  function, p5 should call it repeatedly, etc

* Add support for basic 2D drawing -- creating rectangles, lines,
  points, circles, etc.

* Add utility functions to parse colors, work with mathematics, create
  bezier curves, etc.

* Add support for loading and displaying images.

* Add support for displaying text.

Since I hadn't worked on OpenGL before the GSOC period, we soon ran
into a massive optimization issue at the end of week eight. This meant
that we weren't able to implement image support and text support in
p5.


What needs to be done?
----------------------

Even though we met most of our goals for the GSOC period, p5 is far
from being complete. Before we start adding more features, we would
like to fix issues #9 and #10 first. Right now, p5 is practically
useless on computers running Mac OS. Most sketches stop refreshing
after drawing a couple of frames. Since I do most of the development
work on a linux machine, I haven't been able to debug this properly.
We would really appreciate help from mac users who are willing to test
things out for us and help us debug this.

Our end goal is to implement the full Processing API in Python,
however, we would like to focus on the following features in the next
couple of months:

* Add support for live coding of sketches through the python REPL.
* Add support for images.
* Add support for text and fonts.


Using p5, links, etc
--------------------

p5 was released on the PyPI and can be installed using pip. For
complete installation instructions, see the `installation page
<http://p5.readthedocs.io/en/latest/install.html>`_ on the
documentation. To know more about the project, use the following
links:

* `Documentation <http://p5.readthedocs.io/en/latest/>`_
* `Project source code <https://github.com/p5py/p5>`_
* `Project home page <http://p5py.github.io/>`_
* `Repository with example p5 sketches <https://github.com/p5py/p5-examples>`_
