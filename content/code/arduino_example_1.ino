// Arduino Code for Example 1
// (arduino_example_1.ino)

const int ledPin = 13;
void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}
void loop()
{
  if (Serial.available())
  {
    char inputValue = Serial.read();
    if(inputValue == 'H')
    {
      digitalWrite(ledPin, HIGH);
    }
    else if(inputValue == 'L')
    {
      digitalWrite(ledPin, LOW);
    }
    else
    {
      // we will do nothing if the data is
      // anything other than a ‘H’ or a ‘L’
    }
  }
  delay(10);
}
