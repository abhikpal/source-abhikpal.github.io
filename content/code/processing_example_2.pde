// Processing Code for Example 2
// processing_example_2.pde

import processing.serial.*;

Serial arduinoPort;

float barLength = 0;

void setup()
{
  size(600, 150);
  background(20);
  noStroke();
  fill(220);

  arduinoPort = new Serial(this, "COM5", 9600);
  arduinoPort.bufferUntil('\n');
}

void draw()
{
  background(20);
  rect(25, 25, barLength, 100);
}

void serialEvent(Serial arduinoPort)
{
  String rawInput = arduinoPort.readStringUntil('\n');
  int rawVal = int(trim(rawInput));
  barLength = map(rawVal, 0, 1023, 0, 575);
}
