#include <Servo.h>
Servo s1;
Servo s2;
int data;
void setup()
{
  Serial.begin(9600);
  delay(100);
  s1.attach(A0);
  s2.attach(A1);
  for (int i=0;i<90;i=i+10)
  {
    s1.write(i);
    s2.write(i);
    delay(100);
  }
}
void loop()
{ 
  if (Serial.available()<0){
    data=Serial.read();
      if (data=='a'){
      s1.write(40);
      s2.write(40);
      delay(100);
      }
  }
} 

