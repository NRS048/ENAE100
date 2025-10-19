//HW - Read and display voltage (0V = 0, 5V = 1023)

int readPin = A0; // Declare analog pin used for voltage measurement

int val = 0; // Declare integer variable to store raw voltage measurement

float voltageVal = 0; // Declare float to store voltage (with decimal points) //Could this be a double? safe to assume that voltage will not be negative entering this pin.

void setup()
{
  Serial.begin(9600); // Begin serial communication to laptop

}

void loop()
{
  val = analogRead(readPin); // Measure "voltage" on the readPin, range from 0 - 1023
  voltageVal = val / 204.6; // 1023 / 5 = 204.6, which we can use to convert the large range to the 0-5V expected range
  
  Serial.print("Voltage: "); // Lable to help humans read the data
  Serial.println(round(voltageVal * 100) / 100); // Output data on serial monitor, rounded to 2 decimal places
  
  delay(100); // delay of 100 microsecods to slow down data flow, and make easier to read

}
