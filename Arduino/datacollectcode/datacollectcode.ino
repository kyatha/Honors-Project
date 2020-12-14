

#include <EmonLib.h>
EnergyMonitor emon1;

void setup() {

  Serial.begin(9600);
  
  emon1.current(A0, 111.1); 

  //excel set up
  Serial.println("CLEARSHEET");
  Serial.println("LABEL,Timer,Current"); 
  Serial.println("RESETTIMER"); //resets timer to 0
}

void loop() {
    float Irms = emon1.calcIrms(1480);
  
  Serial.print("DATA,TIMER,");
  Serial.print(Irms);
  Serial.println(); 
  delay(1000); 
}
