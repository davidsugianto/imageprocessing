#include <Servo.h>
#include <LiquidCrystal.h>
Servo s1;
Servo s2;
int x,y,radius;
int sudut1=30,sudut2=30;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup()
{
  Serial.begin(9600);
  delay(10);
   lcd.begin(16, 2);
  s1.attach(A0);
  s2.attach(A1);
  for (int i=1;i<50;i++)
      {
        s1.write(i);
        s2.write(i);
        delay(50);
      }  
  s1.write(sudut1);
  s2.write(sudut2);
}
void loop()
{
  if (Serial.available()>=3)
    {
      x=Serial.read();
      y=Serial.read();
      radius=Serial.read();
    }
  if(x==0&&y==0&&radius==0)
   {
   
   lcd.setCursor(0,1);
   lcd.print("tidak ada bola");
   } 
  else {
   lcd.setCursor(0,0);
   lcd.print(x);
   lcd.setCursor(5,0);
   lcd.print(y);
   lcd.setCursor(10,0);
   lcd.print(radius);
  }
  
}
   
   void coba()
  {
    if (x>60)
  {
    sudut1=sudut1+5;
    s1.write(sudut1);
  }
  else if(x<60)
  {
    sudut2=sudut2-5;
    s1.write(sudut2);
  }
  if (sudut1<=10)
   {
    sudut1=10;
   }
  if(sudut1>=70)
   {
    sudut1=70;
   } 
   if (y>60)
  {
    sudut1=sudut1+5;
    s2.write(sudut2);
  }
  else if(y<60)
  {
    sudut2=sudut2-5;
    s1.write(sudut2);
  }
  if (sudut2<=10)
   {
    sudut2=10;
   }
  if(sudut2>=70)
   {
    sudut2=70;
   } 
  }   
