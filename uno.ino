void setup() {
  Serial.begin(9600);

}

void loop() {
  if (Serial.available() > 0){
    
    int comando = Serial.read();
    
    if(comando == 76){
      Serial.println("Liga a luz.");
    }else{
      Serial.println("Desliga a luz.");
    }
    
  }

}
