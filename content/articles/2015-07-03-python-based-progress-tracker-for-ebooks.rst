A Python Progress Tracker for Kindle
====================================

:date: 2015-07-03 00:46:12 +0530
:tags: python, matplotlib, books
:comments: True

Is our reading pace consistent throughout a book? Or are there parts where we speed up and parts where we slow down? Here is a mini Python hack to investigate that using Amazon's kindle.

The final results are graphs that help you answer:

- How fast did I read that book?
- How long was each reading session?
- Where did I take the most number of notes/highlights/bookmarks?

.. image:: /images/PyProgTracker.png
    :alt: sample run on my clippings from Stoker's 'Dracula'

This should have been slightly easier. Unfortunately, Amazon doesn't allow you to write custom apps for your own Kindle. Which means that the only way to add this feature was jailbreak my small little device and possibly risk bricking it. Reluctant to try that path first, I decide to look for alternatives.

The result was a Python script that does the plotting for you (screenshot above). Once the kindle is connected, a bash script gets the ``My Clippings.txt`` file from your Kindle. The python script then takes this file, uses some regular expressions to locate the required timestamps, and finally uses these times stamps to plot your progress through a book [#]_. 

The script has been refactored and now hides resides `here <https://github.com/abhikpal/ebook_utils>`_ [#]_. One thing though, this only works if you consistently take notes on your kindle, highight stuff, or bookmark things.


.. [#] I guess the project is simple enough to be implemented in JavaScript and I should try porting it to use d3.
.. [#] It's quite sad; ``ebook_utils`` was the best name I could come up with.
