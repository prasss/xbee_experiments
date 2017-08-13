import time
import serial
                          # calling for time to provide delays in program
ser = serial.Serial('/dev/ttyUSB1',9600)

while 1:
      x=ser.readline()
      x = int(ser.readline())
     # print x
      time.sleep(0.1)
      if x==3:
       print("right mare")
      if x==1:
       print("left mare")
      if x==2:
       print("middle mare")
