import serial
import time

port = "/dev/ttyUSB0"  # Adjust if needed
baudrate = 9600       # Check sensor's documentation

ser = serial.Serial(port, baudrate)

print("connected to: " + ser.portstr)
count = 1

while True:
    print("ser", ser)
    print("ser.read()", ser.read())
    print("ser.readline()", ser.readline())
    for line in ser.read():

        print(str(count) + str(': ') + chr(line))
        count = count+1

ser.close()

