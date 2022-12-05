#include <Wire.h>
// Controlar o LED da própria placa Arduino
const int ledPin = LED_BUILTIN;
void setup() {
    Wire.begin(0x8);
    //Reporar “receiveEvent” quando receber dados
    Wire.onReceive(receiveEvent);
    // Define o pino do LED como saída e o desliga
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
}

// Função executada sempre que dados são recebidos do controlador (Raspberry Pi)
void receiveEvent(int howMany) {
    while (Wire.available()) { // loop
        char c = Wire.read(); // recebe o byte como char
        digitalWrite(ledPin, c);
    }
}

void loop() {
    delay(100);
}