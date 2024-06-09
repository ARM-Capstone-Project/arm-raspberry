import serial
import time
print("library imported!!!")
port = "/dev/ttyUSB0"  # Adjust if needed
baudrate = 115200       # Check sensor's documentation

ser = serial.Serial(port, baudrate)
print("ser initialized!!!")

try:
    print("try!!!")
    while True:
        print("ser", ser)
        print("ser.readline()", ser.readline())
        print("ser.readline().decode()", ser.readline().decode())
        print("ser.readline().decode().strip()",
              ser.readline().decode().strip())
        data = ser.readline().decode().strip()
        if data:
            print("data", data)
            # Process the data based on sensor's output format
            if data == "ON":
                print("Object detected!")
            elif data == "OFF":
                print("No object detected.")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("except!!!")
    ser.close()

