************************************************************
Getting Started With Arduino-Processing Serial Communication
************************************************************

:date: 2013-10-05 12:29:27 +0530
:tags: arduino, processing
:comments: True

:summary: A longish tutorial on getting started with Arduino-Processing serial communication.
:cover: /assets/images/posts/arduino_processing_interact/cover.JPG

This (slightly long) tutorial will try to get a beginner started with Arduino Processing communication. This tutorial assumes that you know how to perform basic operations like uploading sketches, writing and compiling Arduino code, and some basics of processing.

The code discussed in this tutorial can be found `here <http://gist.github.com/abhikpal/6822845>`_.


Gathering what you need
=======================

Hardware
--------

There are a very few things that you need for performing a basic Arduino-Processing communication. Most probably you will have the major part of the components lying around you. But still (for some reason still unknown to me!), I think it is better to go through the list once. So in no particular order, these are the things you will need:

An Arduino Board
^^^^^^^^^^^^^^^^

.. image:: /images/arduino_processing_interact/freeduino.JPG
    :alt: Arduino
    :width: 50%

The original Arduino boards come in many flavors, from small Arduino Micros to large Arduino Megas. Arduino clones on the other hand have a different story; these boards function like an Arduino would but often have more features and are the cheaper alternatives to an official Arduino board. For this tutorial I'm going to use Freeduino USB Arduino compatible board designed by some guy at Probots (<http://www.probots.co.in>).

An LED
^^^^^^
.. image:: /images/arduino_processing_interact/led.JPG
    :alt: LED
    :width: 50%

These are the small things that light up here and there in almost every electronics project. I'm using a standard 5mm red LED for this tutorial but LEDs of other color or even buzzers can be used. The use of the LED is optional as most of the Arduino boards have one connected on pin 13.

A Potentiometer
^^^^^^^^^^^^^^^

.. image:: /images/arduino_processing_interact/pot.JPG
    :alt: Potm
    :width: 50%

In addition to a LED and an Arduino you will need a potentiometer to act as a simple input device. We will use this potentiometer in Topic 2 to control a simple visual on our computer screen. I recommend that you solder wires to your potentiometer, because it makes them easy to connect and use. I will use a 10K rotatory potentiometer in this tutorial, but other sensors like LDRs, Infrared proximity sensors, Microphones or SONAR can also be used with appropriate change in the circuitry and code.

A 3V Coin Cell
^^^^^^^^^^^^^^

.. image:: /images/arduino_processing_interact/coin_cell.JPG
    :alt: coin_cell
    :width: 50%

This is not exactly a necessity but having a 3V cell will help you test you LEDs or check for their polarity or make some small and awesome LED throwies(<http://makezine.com/projects/extreme-led-throwies/>)

In addition to these you will need a USB cable to connect your Arduino to your computer and a soldering iron to solder wires to your potentiometer.

Software
--------

The two programs you will need for thus tutorial are the Arduino IDE which can be found by navigating to the 'Downloads' page at <http://www.Arduino.cc>. Depending on your choice you can download either of the Arduino installer or the ZIP archive. It is freely available and open source.

.. image:: /images/arduino_processing_interact/arduino_download.png
    :alt: arduino_website

The second software is the Processing IDE, which too like the Arduino IDE is open sourced and can be downloaded for free by following the 'Downloads' link at http://www.processing.org .

.. image:: /images/arduino_processing_interact/processing_download.png
    :alt: processing_website

Sending data to your Arduino board
==================================

Sending data from your processing sketch to control the state of a LED on your Arduino.

Making the Circuit
------------------

If your Arduino has a led connected to pin 13, you can jump directly to the coding section.

The circuit is super simple and you will need your Arduino board and a LED to make it. Disconnect power from your Arduino before you start making your circuit.

.. image:: /images/arduino_processing_interact/led_test.JPG
    :alt: coin_cell_test

First test your LED using a 3V coin cell. Now, connect the longer lead (positive terminal) of the LED to pin 13 of your Arduino, the shorter lead (negative terminal) goes to the GND (Ground) pin near pin 13. If your LED has both the leads of equal length, identify the positive and the negative terminals using the 3V coin cell. Below are the computer generated and actual set up of the circuit:

.. image:: /images/arduino_processing_interact/Processing_Arduino_1_bb.png
    :alt: ard_circ

.. admonition:: Update
  
    As  `Grumpy_Mike <http://forum.Arduino.cc//index.php?action=profile;u=5282>`_ pointed out in the Arduino forum post (<http://forum.Arduino.cc//index.php?topic=191586.0>) regarding this tutorial, a current limiting resistor (330 ohms will work fine) should be added between the shorter lead of the LED and the Arduino ground pin. You can however directly attach the LED to the ground pin if your Arduino has a current limiting resistor connected on pin 13 (most of the older Arduinos have one attached, and the clone I'm using is one of them). 

.. image:: /images/arduino_processing_interact/Slide1.JPG
    :alt: ard_circ_

The Arduino Code
----------------

Open your Arduino IDE and you are ready to start coding.

We start by allocating a variable name to our LED and setting it as output. This can be achieved by typing the following code snippet:

.. code-block:: cpp

    const int ledPin = 13;

    void setup()
    {
      pinMode(ledPin, OUTPUT);
    }

    void loop()
    {
    }


Now, to communicate with our processing sketch we need to initialize the serial communication; this we do by calling the ``begin()`` method on the ``Serial`` object. The syntax used for initializing the serial port is:

.. code-block:: cpp

    Serial.begin(baud_rate);

Baud is a variable unit of data transmission speed, or simply 1 baud = 1 bit per second. The term 'baud' comes from the name of a French inventor J. M. E. Baudot. A baud rate of 9600 will be fine for us. So the final line of code that we have to include in our ``setup()`` function is :

.. code-block:: cpp

    Serial.begin(9600);

Once our serial port is initialized we need to check for any available data. So, in our ``loop()`` function we use a simple if statement to check if there is any available data.

.. code-block:: cpp

    if(Serial.available())
    {
    }

If data is available in the serial buffer the condition ``Serial.available()`` evaluates to true and the if-block is executed.

We have opened up the serial port, checked for data availability, so our next job is to actually use the data. We will declare a variable of type ``char`` called ``inputValue`` and assign it to the data available in the serial buffer. We do this operation by using:

.. code-block:: cpp

    char inputValue = Serial.read();


The ``read()`` method takes the data available in the Serial buffer and stores it in our ``inputValue`` variable. This statement is typed inside the if-bock we discussed before.

Now, if the data we receive is ``H`` we will turn on the LED if it is ``L`` we will turn off the LED, if it is neither ``H`` or ``L`` we do nothing. So we add the following lines after storing the value to exhibit this behavior:

.. code-block:: cpp

    if(inputValue == 'H')
    {
      digitalWrite(ledPin, HIGH);
    }
    else if(inputValue == 'L')
    {
      digitalWrite(ledPin, HIGH);
    }
    else
    {
      // we will do nothing if the data is
      // anything other than a 'H' or a 'L'
    }

Finally at the end of the ``loop()`` function we will add a small ``delay()`` of 10 milliseconds to avoid overloading the Arduino with data.

The final code if you have followed along should look something like this:

.. code-include:: ../code/arduino_example_1.ino
    :lexer: cpp

Once the code is written upload it to your Arduino, and open the Serial Monitor. Try sending the values to your Arduino like ``H``, ``L`` or anything else. The LED should light up every time you send an ``H`` and should turn off when you send a ``L``.

.. image:: /images/arduino_processing_interact/arduino_example_1.png
    :alt: ard_1

Processing Code
---------------

We start by importing the serial library for processing and setting up a basic sketch.

.. code-block:: java

    import processing.serial.*;
    void setup()
    {
      size(400, 400);
      background(20);
      fill(100);
      noStroke();
    }
    void draw()
    {
    }

In order to send data through the serial port we need to first create an object of the Serial class. So we add the following line to our sketch after the import line.

.. code-block:: java

    Serial arduinoPort;

Now inside the ``setup()`` function we initialize the arduinoPort object we created.

.. code-block:: java

    arduinoPort = new Serial(this, "COM5", 9600);

``this`` is used to indicate that it is the current sketch that is going to talk to Arduino, ``9600`` is the baud rate and ``COM5`` is the COM port to which our Arduino is connected. You need to change the COM port to the port your Arduino is connected.

Now, in the ``draw()`` function we will draw a simple button, clicking the button will cause the led to light up and taking the mouse cursor out of the button will cause the LED to turn off. We draw our button using a simple rectangle.

.. code-block:: java

    rect(150, 150, 100, 100);

To check if the mouse cursor is inside our button we add a simple ``if-else`` block

.. code-block:: java

    if ((mouseX > 150) && (mouseX < 250) && (mouseY > 150) && (mouseY < 250))
    {
    }
    else
    {
    }

In Processing ``mouseX`` and ``mouseY`` are keywords and return the current mouse coordinates. So using them without any declaration will not cause any errors.

If the mouse cursor is inside our box we need to check if the mouse button is pressed (The term mouse button if not explicitly stated refers to the left mouse button) also, we need to change the color of the box to make the program a bit more interactive and intuitive to use. Therefore inside our 'if' block we insert the following code fragment:

.. code-block:: java

    fill(220);
    if (mousePressed == true)
    {
    }

Like ``mouseX`` and ``mouseY`` the ``mousePressed`` keyword returns the state of the left mouse button i.e. ``0`` if not pressed and ``1`` if pressed. So whenever we press the mouse button inside the button the sketch will execute the program statements inside the second ``if`` block. What we have to do now is send a command to the Arduino to light up the LED which we defined in the Arduino sketch to be a ``H`` character so inside our second ``if`` block we will add:

.. code-block:: java

    port.write('H');

This statement sends an ``H`` character to our Arduino. The method ``write()`` writes the arguments inside the parenthesis to the object on which it is called. i.e if we type

.. code-block:: java

    port.write(someValue);

It will write the contents of the variable ``someValue`` to the ``port`` object.

Finally we need to add some command which switches off the led when we take our mouse outside the button and change its color back to normal. So inside out outermost else block we will type:

.. code-block:: java

    fill(100);
    arduinoPort.write('L');

With your Arduino connected try running the processing sketch, you should see the LED light up every time you click inside the box and go off once you put your mouse out of the box. You should see something similar to the screen shot below:

.. image:: /images/arduino_processing_interact/processing_example_1.png
    :alt: prs_1


If something is wrong take a look at the completed code below:

.. code-include:: ../code/processing_example_1.pde
    :lexer: java

Sending Data from the Arduino to a Processing Sketch
====================================================

Making the Circuit
------------------

In Topic 1 we sent data from our computer to the Arduino and make a light turn on and off. This time we will do it the other way round i.e. from the Arduino to the computer.
To begin with the circuit construction solder wires to your pot meter.
A computerized version of the circuit is shown below

.. image:: /images/arduino_processing_interact/Processing_Arduino_2_bb.png
    :alt: ard_2

First, connect the two outer most wire to pins GND (Ground i.e. 0V) and the other to 5V pin. The middle wire aka the wiper should go to the pin marked A0

This way of connecting the pot meter insures that the potential difference (aka voltage) between the GND pin and 'A0' is always a value between 0V and 5V. This setup can also be considered as an example of a simple `Voltage Divider <http://en.wikipedia.org/wiki/Voltage_divider>`_.

the actual circuit is shown below

.. image:: /images/arduino_processing_interact/Slide2.JPG
    :alt: ard_2_

Arduino Code
------------

Like the previous Arduino code we strat by creating a basic sketch and initializing the Serial port.

.. code-block:: cpp

    void setup()
    {
      Serial.begin(9600);
    }

    void loop()
    {
    }

Now, we declare a variable to store the pin number of our pot-meter. We can assign a value of 'A0' to an int but to make it look more int-like I'm going to assign a value of 14 to our potPin variable (the numbering scheme for 'Analog In' pins is quite simple, after digital Pin 13 A0 becomes 14, A1 becomes 15 and so on...)

.. code-block:: cpp

    const int potPin = 14;

The 'Analog In' pins are pre-configured as inputs so adding something like

.. code-block:: cpp

    pinMode(potPin, INTPUT);

would be completely useless.

We now need read the pot meter and send the value over the serial port to our processing sketch. Therefore we first declare a variable of type int and assign it the value that we read from our pot meter. To do this add the following codee inside your ``loop()`` function

.. code-block:: cpp

    int potMeterReading = analogRead(potPin);

Next, we need to send the value we just read from our pot meter through the Serial port to our processing sketch. This can be done by:

.. code-block:: cpp

    Serial.println(potMeterReading);

When we send something using the println method a '\n' aka newline character is automatically appended at the end of our data. We will use this '\n' character to later to collect our data in the processing sketch.

Finally, we add a small delay at the end of our code to make the result a bit more noticable while testing the code on the Arduino Serial Monitor.

.. code-block:: cpp

    delay(100);

In case you missed something here is the completed code:

.. code-include:: ../code/arduino_example_2.ino
    :lexer: cpp

Once you have checked and compiled your code upload it to your Arduino, open the Arduino Serial Monitor and try rotating your pot meter. You should see about 10 values pop up each second on your serial monitor indicating the reading of the pot meter.

.. image:: /images/arduino_processing_interact/arduino_example_2.png
    :alt: ard_2_c

Processing Code
---------------

We start by creating a basic processing sketch and initializing the Serial port

.. code-block:: java

    import processing.serial.*;

    Serial arduinoPort;

    void setup()
    {
      size(600, 150);
      background(20);
      noStroke();
      fill(220);
      
      arduinoPort = new Serial(this, "COM5", 9600);
    }

    void draw()
    {
    }

Now, we declare a global vaiable ``barLength`` just before or ``setup()`` function; this variable will store the current length of the rectangle we will display on the screen

.. code-block:: java

    float barLength = 0;

In our ``draw()`` method we have to draw a rectangle with its length equal to ``barLength``. To do this we simply add:

.. code-block:: java

    rect(25, 25, barLength, 100);

Also, the rectangles will be drawn every time the ``draw()`` function is called; so we need to make sure that the screen is clear before we try to draw a new rectangle, as not clearing the screen will cause the rectangles to be drawn on top of each other and smaller rectangles would therefore would be rendered invisible.

So, before the ``rect()`` function we just called in our ``draw()`` function; add the following line of code:

.. code-block:: java

    background(20);

We are done setting up the basic interface for our little program. Lets start to code the actual mechanism that will interpret the values received from the Arduino

Before we do anything with the data our Arduino is sending us we need to extract the useful information from the stream of data the Arduino is sending. As discussed in Section 2.2 of this tutorial we are going to use the'\n' (newline) charcter to distinguish between different sets of data the Arduino is sending.

To check when we receive the newline charcter we will use the ``bufferUntil()`` mrthid and call it on our arduinoPort object we just created. So, in the ``setup()`` function after the Serial port initialization add this line:

.. code-block:: java

    arduinoPort.bufferUntil('\n');

The line we just added will call another function called the serialEvent whenever a '\n' is detected in the stream of data. The basic syntax for using the bufferUntil method is:

.. code-block:: java

    port.bufferUntil(search_term);

Now we will add the ``serialEvent()`` fuction we just discussed. To do this type the following block of code after your ``draw()`` function

.. code-block:: java

    void serialEvent(Serial arduinoPort)
    {
      
    }

The ``serialEvent()`` function takes a object of type Serial as its parameter (which many of you might have noticed)

All we need to do now is to get the value from the Arduino convert it to a type which we can use in our program. To extract the value we will declare a temporary variable of type String to store the raw values sent by the Arduino. We do this by adding

.. code-block:: java

    String rawInput = arduinoPort.readStringUntil('\n');

to our ``serialEvent()`` function. This line of code stores all the values it reads from the arduinoPort object upto (but not including) the ``'\n'`` character into a string which we have named ``rawInput``

Next, we need to remove any white spaces that might have found their way into the dat a and convert the resultant string to an int. Finally we will map the values the Arduino is sending from a 0 to 1023 scale to a 0 to 575 scale in order to prevent our rectangle to escape the screen if the value gets too large.

So just after the line we added, we add the last two lines of our code

.. code-block:: java

    int rawVal = int(trim(rawInput));
    barLength = map(rawVal, 0, 1023, 0, 575);

In the above two lines we first trim the String rawInput to remove any white spaces using the ``trim()`` function. Then we use type casting to convert the value of the trimmed string to an int using the ``int()`` syntax. Finally we map the value received after type casting from a range of 0 to 1023 to a range of 0 to 575 i.e. our maximum barLength

Here is the completed code in case you missed something:

.. code-include:: ../code/processing_example_2.pde
    :lexer: java

with your Arduino connected to your computer run the code. You will see a window similar to one shown below pop up and on turning the pot-meter you will see the length of the rectangle change.

.. image:: /images/arduino_processing_interact/processing_example_2.png
    :alt: prs2_c

Phew! that was one long tutorial and hopefully you got to know how to perform a basic Arduino-Processing Communication. Now, you can use this knowledge to build spaceships, time machines, control robots from the internet, connect your gadgets to the net and some other cool stuff.

Feel free to post any queries, suggestions, corrections or any other related stuff in the comments below :).
