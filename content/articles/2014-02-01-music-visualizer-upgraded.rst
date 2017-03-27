Music Visualizer Upgraded
=========================

:date: 2014-02-01 15:35:23 +0530
:tags: arduino, processing
:comments: True

:summary: Polishing the last music visualizer project to grab audio data from the computer's output channel using the inbuilt 'Stereo Mix' recording device in Windows.

I had made a simple `music visualizer <{filename}2014-01-16-simple-music-visualizer.rst>`_ and it had its own set of drawbacks; the most irritating one being that whenever I wanted to play a file I would have to follow the absurd ritual of putting a the new file in the folder containing the Processing sketch, change code, run the code again and then see the file "visualized". I definitely needed a way to make the Processing sketch automatically detect any sound being played and then send the required values to the Arduino.

I used the method as `described <http://forum.arduino.cc/index.php?topic=211332.0>`_ by Arduino forum user `macegr <http://forum.arduino.cc/index.php?action=profile;u=5310>`_ who did a similar `project <http://www.macetech.com/blog/node/111>`_ back in 2011.

To achieve what we want to do i.e. respond to sound events from any program we will redirect the output to a special kind of recording mode available in Windows (I don't know about other operating systems, use Google) called "Stereo Mix". It's main purpose in life is to fetch any sound from the output channels and then use the same sound to act as input. It is something like placing a microphone against your speaker to record whatever sound your speaker produces; just with negligible noise and without any special hardware.

Setting up Stereo Mix
---------------------
 
.. image:: /images/music_visualizer_2/stereo_mix_2.png
    :alt: Step 2
    :width: 50%

The setup should be straight forward. Start by right click on the speaker icon in the taskbar and select 'Recording Devices' from the menu that appears.

.. image:: /images/music_visualizer_2/stereo_mix_3.png
    :alt: Step 3
    :width: 50%

You will see a window similar to the one shown above.

.. image:: /images/music_visualizer_2/stereo_mix_4.png
    :alt: Step 4
    :width: 50%

Right click on any blank area and select "Show Disabled Devices". This should give you a list of devices.

.. image:: /images/music_visualizer_2/stereo_mix_5.png
    :alt: Step 5
    :width: 50%

Right click on "Stereo Mix" and select "Enable"

.. image:: /images/music_visualizer_2/stereo_mix_6.png
    :alt: Step 6
    :width: 50%

Now, click on "Stereo Mix" to select it and then click on the "Set Default" button.

.. image:: /images/music_visualizer_2/stereo_mix_7.png
    :alt: Step 7
    :width: 50%

You should see the check mark shift from you default device to "Stereo Mix"

.. image:: /images/music_visualizer_2/stereo_mix_8.png
    :alt: Step 8
    :width: 75%

To ensure that you have done everything right, open up a sound file and play it. You should see the sound level indicator near the "Stereo Mix" icon change according to whatever you are playing.

Processing Code
---------------

Most of the code remains the same. The parts handling the audio channels now take input from the computer's recording device instead of an mp3 file in the folder.

.. code-include:: ../code/visualizer01.pde
    :lexer: java

Upload the Dimmer example to your Arduino board and run the Processing sketch. Turn up the volume and try playing some sound files on your computer, they need not be located in the same folder as your Processing sketch. You should see the wave-forms in the Processing sketch change and your LED flash accordingly.

.. image:: /images/music_visualizer_2/main.png
    :alt: Final Step
