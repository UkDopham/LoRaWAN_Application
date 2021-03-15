void setup() {
  SerialUSB.begin(57600);
  Serial2.begin(57600);
}

void loop() {
  writeHello();
}


void writeHello(){
  //SerialUSB.write("hello");
  delay(1000);
}
