#include <LiquidCrystal.h>
  LiquidCrystal lcd(14,15,16,17,18,19);
void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
  delay(10);
  lcd.setCursor(0,0);
  //lcd.print('A');
  //delay(1000);

}
void loop()
{
  Serial.write('A');
    if ( Serial.available()>0){
      lcd.setCursor(0,0);
      lcd.print(Serial.read());
    }
  delay(100);
}
      
  
