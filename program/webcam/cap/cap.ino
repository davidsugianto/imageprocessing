#define batPin A0;

void setup()
{
  pinMode(A0,INPUT);
  pinMode(A1,OUTPUT);
  Serial.begin(9600);
  digitalWrite(A0,LOW);
  digitalWrite(A1,LOW);
}

float volt1()
{
  float analog = analogRead(A0);
  float volt = analog * (5.0/1023);
  return volt;
}

void loop()
{
  float a=volt1();
  Serial.print(a);
  Serial.println();
  if (a >= 4.99)
  {
    delay(800);
    digitalWrite(A1,HIGH);
  }
  else if (a <= 4.50)
  {
    digitalWrite(A1,LOW);
  }  
}
/*{
  int data=analogRead(A5);
  Serial.print(data);
  Serial.print("=");
  if (data >=100)
  {
    Serial.println("1");
    digitalWrite(4,1);
  }
  else
  {
    Serial.println("0");
    digitalWrite(4,0);
  }
  
}*/
