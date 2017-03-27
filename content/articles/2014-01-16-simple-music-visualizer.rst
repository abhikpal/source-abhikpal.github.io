Simple Music Visualizer
=======================

:date: 2014-01-16 22:05:32 +0530
:tags: arduino, processing
:comments: True

:cover: /images/music_visualizer/cover.png
:summary: A simple Arduino-Processing based music visualizer that puts the glowdrons to some good use.

.. note::
    
    If you are new to serial communication between Arduino and Processing you refer to the (slightly long) tutorial `here <{filename}2013-10-05-interfacing-arduino-from-processing.rst>`_.

In my last post I made a `glowing dodecahedron <{filename}2014-01-01-glowdrons.rst>`_ out of paper and some glue. In this project I convert the same dodecahedron to make a super simple music visualizer using Processing and Arduino.

.. figure:: /images/music_visualizer/dodec.jpg 
    :alt: dodecahedron
    :width: 50%

This project uses only one color of the RGB LED i.e., you can substitute the RGB LED with a usual LED. (Using the RGB LED? The wiring diagrams are on the `dodecahedron post <{filename}2014-01-01-glowdrons.rst>`_.

This is way simpler than Adafruit's `Piccolo <http://learn.adafruit.com/piccolo>`_ and all it does is change the brightness of the LED based on average of the values sent to the left and right audio channels. The processing sketch uses the Minim library (included by default in recent versions of Processing) to get the values out of the audio buffer and make some (weird?) visual on the screen.

We will use the dimmer sketch to convert the values sent by the processing sketch to the equivalent LED brightness. You can upload the example sketch at 'File >> Examples >> 04.Communication >> Dimmer' to your Arduino to do this for you. Make sure to change the  ``ledPin`` variable to the pin number your LED is connected to. Compile and upload the sketch. We can now move to the Processing sketch.

Here is the Processing sketch that we'll be using.

.. code-include:: ../code/visualizer00.pde
    :lexer: java

Before running the sketch you need to save it and place a sound file in the same folder that has your sketch. Also, change ``"song.mp3"`` in

.. code-block:: java

    song = minim.loadFile("song.mp3");

to the file that you want to play. And yes, make changes to the COM port accordingly in the following line:

.. code-block:: java
    
    port = new Serial(this, "COM5", 9600);

Connect your Arduino and run your code in 'Present' mode using the keyboard shortcut :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`R` (or by navigating to 'Sketch >> Present' in the Processing IDE).

Once you run your code, you need to click anywhere in the screen to play/pause the song. If the song is being played; you would see something that resembles the screenshot given below. The white bar on the top indicates the value being sent, the green graph on the bottom shows the average values in the audio buffer and the central visual changes according to the values in the left and right audio channels.

.. image:: /images/music_visualizer/screenshot_4.png 
    :alt: processing sketch screenshot

.. admonition:: update

    Placing the sound file you want to play in the sketch folder everytime can get very tedious very soon. The `upgraded version of the visualizer <{filename}2014-02-01-music-visualizer-upgraded.rst>`_ uses the 'Stereo Mix' recording device to grab eveything from your machine's output audio stream, hence removing the unnessary hassle. The upgraded version can be found here.
