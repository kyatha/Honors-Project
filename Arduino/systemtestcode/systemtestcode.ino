

#include <EmonLib.h>
EnergyMonitor emon1;

void setup() {
  
  Serial.begin(9600);
  
  emon1.current(A0, 111.1); 

}

void loop() {
   float Irms = emon1.calcIrms(1480);
  

  Serial.println(Irms);
  
  delay(2000); 
}
