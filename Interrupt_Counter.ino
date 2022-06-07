//This program counts the no. of interrupts detected in a given time interval
//Prints it to the COM port the arduino is connected to.

unsigned long previousMillis = 0;
unsigned long interval = 1000; //Store count for every 1000ms

volatile int c=0; //This is our counting variable

void setup() {
Serial.begin(115200); //Bud rate
attachInterrupt(digitalPinToInterrupt(2), counter, RISING); //Interrrupt is attached to pin 2
//note the interrupt is taken to be the rising part of voltage
// upon interrupt call counter function
}



int counter() {
c++; //Update counting variable
return c;
}


void loop() {  //This part prints the count every second
  unsigned long currentMillis = millis();

  if(currentMillis - previousMillis > interval)
  {
  Serial.println(c);
  //Update timing variable
  previousMillis = currentMillis;
  c=0;
  }
}
