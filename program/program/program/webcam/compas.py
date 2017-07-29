import smbus
import time
bus = smbus.SMBus(1)
address = 0x60

def bearing():
        bear = bus.read_byte_data(address, 3)
        return bear
while True: 
        bear255 = bearing()      #this returns the value as a byte between 0 and 255. 
        #print bearing
        print bear255
        #time.sleep(1)
