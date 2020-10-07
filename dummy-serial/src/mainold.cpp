/*
#include <Arduino.h>
#include <string.h>
#include <stdint.h>

#define BAUDRATE 11520
#define UPDATE_FREQ 10
#define FAILURE_RATE 0.1

uint8_t initialized = 0;
uint32_t last_update = 0;

uint8_t memeq(char a[], char b[], int len) {
  for (uint8_t i = 0; i < len; i++) {
    if (a[i] != b[i]) {
      return 0;
    }
  }
  return 1;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(11520);
  while(!Serial) {}

}

void loop() {
  if (!initialized) {
    char buf[3];
    char init_message[] = {'a', 'a', 'a'};
    char init_reply[] = {'b','b','b'};
    Serial.readBytes(buf, 3);
    if (memeq(init_message, buf, 3)) {
      Serial.write(init_reply, 3);
      initialized = 1;
    }
    return;
  }

  uint32_t time = millis();
  if (time - last_update > 1000) {
    char buf[4];
    buf[0] = time & 255;
    buf[1] = (time >> 8)  & 255;
    buf[2] = (time >> 16) & 255;
    buf[3] = (time >> 24) & 255;

    Serial.write(buf, 4);
    last_update = time;
  }
}
*/