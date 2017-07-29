
#include <LiquidCrystal.h>


LiquidCrystal lcd(19,18,17,16,15,14);
unsigned int x,y,radius;
void setup() {
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  Serial.begin(9600);
  lcd.print("loading....");
  delay(2000);
  lcd.clear();
  lcd.print("ready..!!!");
  delay(2000);
  lcd.clear();
}
void loop() 
{
 if (Serial.available()>=3)
  {
    radius=Serial.read();
    x=Serial.read();
    y=Serial.read();
    
  }
  lcd.setCursor(0,0);
  lcd.print(radius);
  lcd.setCursor(4,0);
  lcd.print(x);
  lcd.setCursor(8,0);
  lcd.print(y);
  
}
