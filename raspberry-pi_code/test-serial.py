import serial

ser = serial.Serial("COM5", 9600)
while True:
    ser.write(b"Hello")

