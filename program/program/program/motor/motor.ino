#include<Servo.h>
#include <LiquidCrystal.h>
#define forward 'F'
#define stOp 'S'
#define Back 'B'
LiquidCrystal lcd(14,15,16,17,18,19);
Servo serv;
unsigned char pin[9]={2,3,4,5,6,7,8,9,10};
char data,code,sudut=30;
unsigned int i;
int fast_ka=70,   
    fast_ki=70,
    pwm_ka=0,pwm_ki=0 ;

///variable for tunning PID control
int error=0,last_error=0;
int Kp=10;
int Kd=12;
float Ki=1;
int Ts=1;
int max_sped=150; 
int min_sped=30;
int set_point=125;
//variabel data serial
unsigned char recaive;
unsigned int Pid_data;
void setup()
  {
    lcd.begin(16, 2); 
    for(int i=0;i<9;i++)
      { 
      pinMode(pin[i],OUTPUT);
      }
    Serial.begin(9600);
    serv.attach(A0);
    serv.write(1);
    delay(100);
    serv.write(20);
    delay(100);
    lcd.print("loading...");
    delay(2000);
    lcd.clear();
    lcd.print("ready!!");
    delay(2000);
    lcd.clear();
  }
void loop()
  {
    //Serial.write('A');
    if (Serial.available()>0)
    {
        recaive=Serial.read();
        lcd.setCursor(0,0);
        lcd.print(recaive);
        if(recaive == 'B')
          {
                mundur();
          }              
         else if (recaive == 'S')
          {
                Stop();
          }
         else if (recaive == 'F')
          {
            maju();             
          }
      
        }
    }
   
void motor_ka(int cw,int ccw,unsigned int pwm)
   {
    digitalWrite(9,cw);
    digitalWrite(10,ccw);
    analogWrite(8,pwm);
    }
void motor_be(int cw,int ccw,unsigned int pwm)
    {
    digitalWrite(2,cw);
    digitalWrite(3,ccw);
    analogWrite(4,pwm);
    }
void motor_ki(int cw,int ccw,unsigned int pwm)
   {
    digitalWrite(5,cw);
    digitalWrite(7,ccw);
    analogWrite(6,pwm);
   }  
void sumbu_y()
{
  if(code=='y'){
       data=Serial.read();
       if (data>30)
         {
           sudut=sudut+5;
         }
       else if(data<30)
         {
           sudut=sudut-5;
         }
       if (sudut>60)
          {
            sudut=60;
          }
       else if(sudut<1)
          {
            sudut=1;
          }
       serv.write(sudut);
     }
   }
   
int PID(unsigned long pv)
{
 int hasil_PID;    
 error=pv-set_point;
 Serial.print(error);Serial.print("\t");
 hasil_PID=((Kp*error) +((Ki/10)*(error+last_error)*Ts)+((Kd/Ts)*(error-last_error)));
  //hasil_PID=((Kp*error)+((Kd/Ts)*(error-last_error)));
 last_error=error;
 return hasil_PID;
}
void go(unsigned int Read)
{
  unsigned int hasil;
    hasil=PID(Read);
    pwm_ka=fast_ka-hasil;
    pwm_ki=fast_ki+hasil;
     if(pwm_ka > max_sped)
        {
          pwm_ka=max_sped; 
        } 
      else if (pwm_ka < min_sped)
        {
          pwm_ka=min_sped;
        }
         
      if (pwm_ki > max_sped)
        {
          pwm_ki=max_sped;  
        }
     else if (pwm_ki<min_sped)
        {
          pwm_ki=min_sped;
        }
    motor_ka(1,0,pwm_ka);
    motor_ki(1,0,pwm_ki);
    
  
  }
  void Stop()
  {
    motor_ka(0,0,0);
    motor_ki(0,0,0);
    motor_be(0,0,0);
  }
  void maju()
   {
     motor_ka(1,0,255);
     motor_ki(1,0,255);
     motor_be(0,0,0);
   }
   void mundur()
   {
     motor_ka(0,1,50);
     motor_ki(0,1,50);
     motor_be(0,0,0);
   }
   void put_kiri()
   {
     motor_ka(1,0,50);
     motor_ki(0,1,50);
     motor_be(0,1,50);
   }
   void put_kanan()
   {
     motor_ka(0,1,50);
     motor_ki(1,0,50);
     motor_be(1,0,50);
   }
