import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins = [27,14,15]
for a in Pins:
    GPIO.setup(a,GPIO.OUT)
pwm = GPIO.PWM(27, 100)
pwm.start(0)
Low = GPIO.LOW
High = GPIO.HIGH
        
def motor_s(cw,ccw,pwm1):
    GPIO.output(14,cw)
    GPIO.output(15,ccw)
    pwm.ChangeDutyCycle(pwm1)

def muter_e():
    motor_s(0,1,40)    

def muter_we():
    motor_s(1,0,50)

def main():
    muter_e()
    sleep(2)
    muter_we()
    stop()
    

if __name__=='__main__':
        main()

