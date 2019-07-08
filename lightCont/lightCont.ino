#include <Wire.h>
#include <Adafruit_MCP4725.h>
Adafruit_MCP4725 dac;

int volt = 5;
int pin  = 5;



void setup() {
  int baud = 9600;
  // put your setup code here, to run once:
  Serial.begin(baud);
  pinMode(pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  //digitalWrite(pin, HIGH);

  
  if (Serial.available() > 0) {
    Serial.println("Recieved");
    delay(100);

  }
  else {
    digitalWrite(pin, HIGH);
    Serial.write("Nope");
    delay(100);
    

  }
}
