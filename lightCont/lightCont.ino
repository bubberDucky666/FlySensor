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

  
  while (Serial.available()) {   
    int msg = Serial.read();
    Serial.write(msg);
    Serial.write("hi");
    
    //if (msg == 1) {
    digitalWrite(pin, 0);
    Serial.write("Recieved");
    delay(100);
    //}
 
  }
  digitalWrite(pin, HIGH);
  //Serial.write("Nope");
  delay(100);
    
}
