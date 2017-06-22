import serial
import cv2

ser = serial.Serial("/dev/ttyACM1", 115200)

while True:
  xin = input()
  code ="x "
  code = code + str(xin, )
  ser.write(code)

  print(ser.read())