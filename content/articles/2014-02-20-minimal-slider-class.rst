A Minimal Slider Class for Processing
=====================================

:date: 2014-02-20 16:49:12 +0530
:tags: arduino, processing
:comments: True

While putting together my music visualizer, I discovered that there was an inconsistency in the colour values I was sending to the Arduino and the actual colour that the RGB LED produced.

.. figure:: /images/slider.png
    :alt: running the slider class

    Running the slider class

The red channel of the RGB LED seemed to often dominate the other channels and I guess it's probably due to scattering. Since the color red happens to scatter the most, it makes your whole thing inconsistent. The problem is similar to what happens when a picture taken from your camera looks *slightly* different on your computer screen and looks ridiculously stupid when printed out of a inkjet (more on this (+ details) can be found in the  `Color Management Wikipedia article <https://en.wikipedia.org/wiki/Color_management>`_ or  `this 'Leds Magazine' piece <http://www.ledsmagazine.com/articles/print/volume-10/issue-6/features/understand-rgb-led-mixing-ratios-to-realize-optimal-color-in-signs-and-displays-magazine.html>`_)

To play around with this issue, I ended up writing a simple sketch that lets you select the colours on your computer, send them to your Arduino and see the corresponding color on your RGB LED.

The sketch uses a custom *slider* class that facilitates to facilitate the drawing, and data retrival from the sliders. You can use it for other exciting things if you want a stupidly simple slider. The whole thing is around 60 lines long and is produced below (save it as ``slider.pde`` inside the same folder containing your main script):

.. code-include:: ../code/slider.pde
    :lexer: java
    :tab-width: 4

And here are the arduino and processing sketches that use this class (because people are just too lazy to go check github and get the code). The resulting interface should be something very close to the screenshot given above.

The code that should go inside your arduino (change the pins accordingly): 

.. code-block:: cpp
    
    /*
     * RGB Color Mixer
     * Takes value from the Serial port,
     * saves to an array, and writes
     * corresponding values to the RGB LED.
     *
     * Abhik Pal | 11:40, 19th Feb 2014
     */

    // Positions of the R, G and B values
    // on the array
    #define RED     0
    #define GREEN   1
    #define BLUE    2

    // maximum values to be stored
    const int maxVal = 3;

    // the array to store the values
    int colors[maxVal];

    // a var. to keep track of the inserted
    // values
    int counter = 0;


    // arduino pins to which LEDs are attached
    const int red = 9;
    const int green = 10;
    const int blue = 11;

    void setup()
    {
        // setting up the leds as OUTPUT
        pinMode(red, OUTPUT);
        pinMode(green, OUTPUT);
        pinMode(blue, OUTPUT);

        // opening up the serial port @ 9600
        // bauds
        Serial.begin(9600);
    }


    void loop()
    {
        // checking if the serial buffer contains
        // anything
        if(Serial.available())
        {
            // adding the value to the array
            // (value subtracted from 255 as I've got 
            // common anode RGB LED)
            colors[counter] = 255 - Serial.read();
            //incrementing the array counter
            counter++;
            // if the counter approaches the maxVal
            // set it to zero i.e. at the beginning of the 
            // array.
            if(counter == maxVal)   counter = 0;
        }

        // write proper values to the LEDs
        analogWrite(red, colors[RED]);
        analogWrite(green, colors[GREEN]);
        analogWrite(blue, colors[BLUE]);
    }

And similarly, change the ports and stuff in the Processing code below:

.. code-block:: java
    
    /*
     * RGB Color Mixer Processing Sketch
     * Draws sliders on the screen and sends values to the Arduino
     * Gives a preview of the color and cliking the preview prints out
     * the RGB values. 
     *
     * Abhik Pal | 11:49, 19th Feb 2014
     */

    // import the Serial library
    import processing.serial.*;

    // making some sliders
    slider red;
    slider green;
    slider blue;

    // ... and a Serial port
    Serial port;

    // initializing the RGB values to zero
    float redVal = 0;
    float greenVal = 0;
    float blueVal = 0;

    void setup()
    {
      // Setting up the screen
      size(850, 400);
      background(20);

      // opening up the Serial port, change the "COM5" and baud rate
      // to suit your needs
      port = new Serial(this, "COM5", 9600);

      // initializing the sliders
      red = new slider(color(220, 20, 20), 50, 50, 00);
      green = new slider(color(20, 220, 20), 200, 50, 10);
      blue = new slider(color(20, 20, 220), 350, 50, 10);
    }

    void draw()
    {
      // clear everything
      background(20);

      // update the slider position
      // change color to the current color
      red.update(color(redVal, 0, 0));
      green.update(color(0, greenVal, 0));
      blue.update(color(0, 0, blueVal));

      // store the slider values in respective variables
      redVal = red.getVal();
      greenVal = green.getVal();
      blueVal = blue.getVal();

      // write out the values to the Arduino
      port.write(int(redVal));
      port.write(int(greenVal));
      port.write(int(blueVal));


      // draw the preview window
      strokeWeight(5);
      stroke(220, 220, 220);
      fill(redVal, greenVal, blueVal);
      rect(500, 50, 300, 300);
    }

    // print out the values when the mouse is clicked and 
    // released inside the preview area
    void mouseReleased()
    {
      if ((mouseX > 500) &amp;&amp; (mouseX < 800))
      {
        if ((mouseY > 50) &amp;&amp; (mouseY < 350))
        {
          print("R:\t" + redVal);
          print(" G:\t"  + greenVal);
          print(" B:\t" + blueVal);
          println();
        }
      }
    }

All of the code here is also hosted on github and can be found in the repo thing for this blog. There are the Arduino and the Porcessing forums if you end up doing something interesting with this.
