import serial
import time

print("Library imported!!!")

port = "/dev/ttyUSB0"  # Adjust if needed
baudrate = 9600       # Check sensor's documentation

# Try different line endings if necessary
line_endings = ("\n", "\r", "\r\n")

ser = serial.Serial(port, baudrate)
print("Serial initialized!!!")

try:
    print("Entering loop...")
    while True:
        for line_ending in line_endings:
            print("line_ending >>>", line_ending)
            data = ser.readline().decode().strip(line_ending)  # Try different endings
            if data:
                print("Data:", data)
                # Process the data based on sensor's output format
                if data == "ON":
                    print("Object detected!")
                elif data == "OFF":
                    print("No object detected.")
                break  # Exit loop if data is found with any ending

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
