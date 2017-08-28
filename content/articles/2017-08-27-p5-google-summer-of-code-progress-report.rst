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

We were able to meet most of our goals for the summer of code period.
These included:

* [ **COMPLETED** ] Create a system that could work with
  Processing-style sketches i.e., if the user defines a
  :code:`mouse_pressed` function, p5 should be able to automatically
  attach an handler to it, if the user defines a :code:`draw`
  function, p5 should call it repeatedly, etc.

* [ **COMPLETED** ] Add support for for basic 2D drawing -- creating
  rectangles, lines, points, circles, etc. We also added two new
  features to the Processing API:

  * Since tuples, lists, and vectors are often used to store
    coordinates in space, we changed the original Processing API to
    use tuple-like objects by default. So, if a user wants to draw a
    line from :code:`start = (0, 0)` to :code:`end = (100, 120)`, they
    can just call :code:`line(start, end)` instead of
    :code:`line(start[0], start[1], end[0], end[1])`.

  * Added new methods to draw circles and squares.

* [ **COMPLETED** ] Add a color parsing system similar to
  Processing's. We also extend the Processing API using Python's
  keyword arguments so users can use commands like
  :code:`fill(red=255, green=127, blue=51, alpha=127)`.

* [ **COMPLETED** ] Add utility functions to perform basic
  mathematical operations, computing trig-functions, and generating
  points for curves and bezier splines. We also tweaked Processing's
  :code:`PVector` class to make it more intuitive to use. For example,
  the syntax for adding vectors in p5 is :code:`vec_sum = vec_1 + vec_2`
  where :code:`vec_1` and :code:`vec_2` are vectors.

* [ **COMPLETED** ] `Release p5
  <https://github.com/p5py/p5/releases/tag/v0.3.0a1>`_ to the Python
  Package Index.

* [ **COMPLETED** ] Add `example code
  <https://github.com/p5py/p5-examples>`_ and `documentation
  <http://p5.readthedocs.io/en/latest>`_ to help people get started.


We had initially planned on adding support for displaying text and
images, but unfortunately weren't able to do so in the GSOC period.
Before week 8 of the coding period, our code was using immediate mode
rendering and our sketches would slow down under load. Instead of
implementing new features like image support and text support we
decided to address the optimizing issue first and re-wrote the
rendering code to use retained mode rendering and use numpy for all
internal computations.


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


Using p5, links to things, etc
------------------------------

p5 was released on the PyPI and can be installed using pip. For
complete installation instructions, see the `installation page
<http://p5.readthedocs.io/en/latest/install.html>`_ on the
documentation. To know more about the project, use the following
links:

* `Documentation <http://p5.readthedocs.io/en/latest>`_
* `Project source code <https://github.com/p5py/p5>`_
* `Project home page <http://p5py.github.io/>`_
* `Repository with example p5 sketches <https://github.com/p5py/p5-examples>`_
