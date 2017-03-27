Basic Text to Speech Intruder Alert System
==========================================

:date: 2013-09-13 23:38:43 +0530
:tags: arduino, processing
:comments: True

.. sidebar:: Fun Fact
    
    The "cool" logo was designed by a 14-year-old Abhik Pal for his then pretentious blog.

Recently while wandering around the web I came across ``ttslib``, a Processing library developed by the folks over at `local-guru.net <http://www.local-guru.net>`_ that can be used produce speech from a processing sketch (also in a very mechanical "robotic" voice). I ended up using this library with Processing to make a super simple intruder alert system.

The algorithm is as unsophisticated as an unsophisticated algorithm can be. The Arduino gets the reading from the PIR sensor and checks if it is high or low (0 or 1). If the PIR detects something the reading goes to 1 and a message is sent to the processing sketch which then uses the sent data to scream : "Intruder alert".

To build this simple “talking” intruder alert system you will need a PIR sensor, an Arduino, Processing, and the `ttslib` Processing library (available at http://www.local-guru.net/blog/pages/ttslib).

The finished circuit (no magic here) looks like this:

.. image:: /images/intruder_2.JPG
    :alt: finished circuit

Simply connect the sensor to pin 7 of your Arduino and add a LED to pin 13 (adding the LED is trivial so you can skip it). Once the circuit is complete, upload the following code to your Arduino:

.. code-include:: ../code/intruder.ino
    :lexer: cpp

Next, download ttslib (from http://www.local-guru.net/blog/pages/ttslib) and install it (on Windows place the extracted files inside ``Documents/Processing/libraries`` or in your sketchbook location).

Try running the example code available at the site.

If all went fine type in the following code in Processing:

.. code-include:: ../code/intruder.pde
    :lexer: java

.. image:: /images/intruder_1.png
    :alt: the thing running

Now, with the Arduino connected, and speakers turned on; run the Processing code. Waving your hands in front of the PIR sensor will make your computer warn "Intruder Alert!".

That's it. You have built yourself a simple intruder alert system and it is actually "talking". Using the same idea you can expand this project to read data from other sensors and react by making your computer speak other things.

The code has been put on Github gist `here <https://gist.github.com/abhikpal/6550687>`_.
