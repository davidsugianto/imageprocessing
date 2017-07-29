from gpiozero import c
from time import sleep
led = c(17)
#tombol = c(2)
#button.wait_for_press()
led.on()
print 'led hidup'
sleep(10 )
led.off()
print 'led mati' 
sleep(1)
