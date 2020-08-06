#include<SoftwareSerial.h>
SoftwareSerial BT(10,11);

void setup() {
BT.begin(9600);
pinMode(12, OUTPUT); // put your setup code here, to run once:
 }

void loop() {
  // put your main code here, to run repeatedly:
 if(BT.available()>0)
   {     
      char data= BT.read(); // reading the data received from the bluetooth module
      switch(data)
      {
        case 'd': digitalWrite(12, HIGH);break; // when a is pressed on the app on your smart phone
        case 'a': digitalWrite(12, LOW);break; // when d is pressed on the app on your smart phone
        default : break;
      }
      Serial.println(data);
   }
   delay(50);
}
