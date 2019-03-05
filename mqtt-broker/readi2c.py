#coding: utf-8

from smbus2 import SMBus
import time

bus_number  = 2
i2c_address = 0x50

bus = SMBus(bus_number)

digT = []
digP = []
digH = []

t_fine = 0.0

def writeReg(reg_address, data):
	bus.write_byte_data(i2c_address,reg_address,data)


def readData():
	data = []
	for i in range (0xE0, 0xE0+8):
            b = bus.read_byte_data(i2c_address,i)
            data.append(b)

	pres_raw = (data[0] << 0) 
	temp_raw = (data[3] << 0) 
	hum_raw  = (data[6] << 0)  
	print(pres_raw)
	print(temp_raw)
	print(hum_raw)	
	bus.close()
#	compensate_T(temp_raw)
#	compensate_P(pres_raw)
#	compensate_H(hum_raw)

#if __name__ == '__main__':
#	try:
#		readData()
#	except KeyboardInterrupt:
#		pass
