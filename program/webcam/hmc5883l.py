from math import atan2
import smbus
import time
bus=smbus.SMBus(1)
bus.write_byte_data(0x1e,0x00, 0x60)
bus.write_byte_data(0x1e, 0x02, 0x00)
while 1:
	data = bus.read_i2c_block_data(0x1E, 0x03, 6)   
 
        # Convert the data
        xMag = data[0] * 256 + data[1]
        if xMag > 32767 :
                xMag -= 65536
 
        zMag = data[2] * 256 + data[3]
        if zMag > 32767 :
                zMag -= 65536
 
        yMag = data[4] * 256 + data[5]
        if yMag > 32767 :
                yMag -= 65536
 
        heading = atan2(yMag, xMag)
        decAngle = (4.0 + (26.0 / 60.0)) / (180 / 3.14)
        heading += decAngle

        if heading < 0:
                heading += (2 * 3.14)
        if heading > 2 * 3.14:
                heading -= (2 * 3.140)

        degree = heading * 180 / 3.14 

  # Output data to screen
#        print "Magnetic field in X-Axis : %d" %xMag
#        print "Magnetic field in Y-Axis : %d" %yMag
#        print "Magnetic field in Z-Axis : %d" %zMag
#        print "Heading : ", heading
        print "Degree : ", degree

