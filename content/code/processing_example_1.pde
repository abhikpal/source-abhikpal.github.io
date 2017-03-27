// Processing Code for Example 1
// (processing_example_1.pde)
import processing.serial.*;

Serial arduinoPort;
void setup()
{
  size(400, 400);
  background(20);
  fill(100);
  noStroke();
  arduinoPort = new Serial(this, "COM5", 9600);
}
void draw()
{
  rect(150, 150, 100, 100);

  if ((mouseX > 150) && (mouseX < 250) && (mouseY > 150) && (mouseY < 250))
  {
    fill(220);
    if (mousePressed == true)
    {
      arduinoPort.write('H');
    }
  }
  else
  {
    fill(100);
    arduinoPort.write('L');
  }
}
