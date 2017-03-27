Paper Glowdrons
===============

:date: 2014-01-01 00:24:40 +0530
:tags: arduino, processing, origami
:comments: True

:cover: '/images/glowdron/cover.jpg'
:summary: Super bright LEDs + Paper Dodecahedrons.

I had nothing particularly exciting to do for the winter break and needed a way to use the super bright RGB LEDs that I had received recently in mail. I ended up combining some origami with a super bright RGB LED and got these cool looking glowing dodecahedrons, aka 'Glowdrons.' This hybrid, if no one has already named it, I call dibs on the names 'Oritronics,' or 'Electrogami.'

This project combines some basic electronics (Arduino + a super bright LED) with *modular origami* (the kind of origami where you join smaller units to make a larger model. Also known as the "cool" type of origami) It is also stupidly simple. Interested? Follow along.

The fun and time-taking part of the project is the construction of the dodecahedron, so we begin by making our very own paper dodecahedron. You don
t need anything complicated. Get some colored paper (I used black), some white paper (make sure the LED you are using gives out enough light to penetrate this paper), glue, pencil, a ruler, a pair of scissors and a hobby knife.

.. image:: /images/glowdron/stuff_you_need.JPG
    :alt: Stuff you need
    :width: 50%

Start by cutting the colored paper into 30 equal sized squares. I made my squares about :math:`7cm \times 7cm`.

.. image:: /images/glowdron/squares.JPG
    :alt: Squares!
    :width: 50%

To make our dodecahedron we will need about 30 similarly folded structures called "units" or "modules."

Folding one module
------------------


.. image:: /images/glowdron/01.JPG
    :alt: fold_step_01
    :width: 50%

To fold a single module, start with a square sheet of paper

.. image:: /images/glowdron/02.JPG
    :alt: fold_step_02
    :width: 50%

Fold the paper in half as shown in the picture above

.. image:: /images/glowdron/03.JPG
    :alt: fold_step_03
    :width: 50%

Fold down the top edges towards the center fold to make an 'M' shape as shown.

.. image:: /images/glowdron/04.JPG
    :alt: fold_step_04
    :width: 50%

Fold the bottom left corner at a 45 degree angle

.. image:: /images/glowdron/05.JPG
    :alt: fold_step_05
    :width: 50%

Fold down the top right cornet at a 45 degree angle. This step is similar to the previous step.

.. image:: /images/glowdron/06.JPG
    :alt: fold_step_06
    :width: 50%

Make a fold connecting the two dots as shown in the picture above.

.. image:: /images/glowdron/07.JPG
    :alt: fold_step_07
    :width: 50%

After you connect the points indicated in the previous step, you should get something that looks like this picture.

The thing that you just finished making is called a module. You need to make 30 of these to make a complete dodecahedron. 

Assembly
--------


If you observe the module you will find two smaller triangles and two larger triangles, we will use these to create interlocking structures which will come together to form the dodecahedron.

.. image:: /images/glowdron/a_01.JPG
    :alt: assembly_step_01
    :width: 50%

Insert the one of the smaller triangles into the flaps of the bigger triangle.

.. image:: /images/glowdron/a_02.JPG
    :alt: assembly_step_02
    :width: 50%

Add one more module in a similar way to create a vertex.

Once you create a vertex keep adding modules to the free ends of the vertex. After joining about 10 modules you should be left with a pentagonal face that looks something like the picture below.

.. image:: /images/glowdron/a_03.JPG
    :alt: assembly_step_03
    :width: 50%

Use your pencil to trace out the pentagon on the white sheet of paper.

.. image:: /images/glowdron/a_04.JPG
    :alt: assembly_step_04
    :width: 50%

Cut out this pentagon making sure that you leave some border outside, this need not be perfect because we will stick it inside our face to act as windows for the light to go out.

.. image:: /images/glowdron/a_05.JPG
    :alt: assembly_step_05
    :width: 50%

Apply some glue to the borders of the face from the inside.

.. image:: /images/glowdron/a_06.JPG
    :alt: assembly_step_06
    :width: 50%

Stick the piece of white paper that you just cut on this side.

.. image:: /images/glowdron/a_07.JPG
    :alt: assembly_step_07
    :width: 50%

Continue adding modules and sticking white paper. Leave at least one side that has no white paper attached to it. This will allow us to install the dodecahedron on top our LED. Once the assembly is complete you should have a paper dodecahedron. Mine looked like the one below.

.. image:: /images/glowdron/dodec_final.JPG
    :alt: final dodecahedron
    :width: 50%

Now, we have our dodecahedron all we need to do now is add some *"glow"* to it.


Adding "glow"
-------------


.. image:: /images/glowdron/DSCN1089.JPG
    :alt: ards
    :width: 50%

To make the dodecahedron glow, I used a 220 Ohm resistor, a super-bright common anode RGB LED, some wire pieces, an Arduino clone, and a proto-shield with a mini bread-board. you can eliminate the proto shield and make the circuit on a breadboard or perf-board instead.

.. image:: /images/glowdron/DSCN1086.JPG
    :alt: compo
    :width: 50%

If you are using the shield start by attaching it to your Arduino.

.. image:: /images/glowdron/DSCN1090.JPG
    :alt: restr
    :width: 50%

As the LED I used was a common anode RGB led meaning that all the LEDs inside the RGB LED share the same positive power supply. So, connect the resistor from the 5V rail to the breadboard.

.. image:: /images/glowdron/DSCN1091.JPG
    :alt: restr
    :width: 50%

Similar to LEDs and ICs you can identify the first pin of the RGB LED from the corner which looks a bit different from the others. You can figure out the pin mapping yourself using a 3V battery or consult the datasheet for the LED you are using. The pin mapping of the LED I used is shown below. notice that the red lead has got a different corner.

.. image:: /images/glowdron/DSCN1087.JPG
    :alt: instr_led1
    :width: 50%

Connect the LED to your breadboard by aligning the common anode to the point where you connected the resistor. I found it easier to insert the LED by rotating it at about 45 degrees.

.. image:: /images/glowdron/DSCN1094.JPG
    :alt: instr_led2
    :width: 50%

Now, connect the red, green and blue leads to the pins that you wish to use. I used the pins 9, 10, 11 to connect the red, green and blue pins respectively.

.. image:: /images/glowdron/DSCN1096.JPG
    :alt: instr_led3
    :width: 50%

Finally, cover your LED using the dodecahedron you just made.

.. image:: /images/glowdron/DSCN1102.JPG
    :alt: final
    :width: 50%

Load some code to control your LED and there you have it, your very own paper dodecahedron. You can try the same thing with other structures like cubes or tetrahedrons. Google "modular origami" to get some nice things you can do with paper.

Happy 2014.
