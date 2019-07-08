#include <Adafruit_MCP4725.h>

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

  int mes = Serial.read();

  if (mes == 1) {
    dac.setVoltage(volt, false);
  }
  else {
    dac.setVoltage(0, false);
  }
}
