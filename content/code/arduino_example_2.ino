// Arduino Code for Example 2
// (arduino_example_2.ino)

const int potPin = 14;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int potMeterReading = analogRead(potPin);
  Serial.println(potMeterReading);
  delay(100);
}
