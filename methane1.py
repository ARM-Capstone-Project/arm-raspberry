import serial
import time

# Serial Port Configuration
serial_port = '/dev/ttyUSB0'  # Adjust if your adapter uses a different port
baudrate = 9600                # Common baud rate, but check your device's specs
timeout = 1                   # Timeout in seconds

# Open Serial Connection
ser = serial.Serial(serial_port, baudrate, timeout=timeout)

# Function to send and receive data
def send_and_receive(command):
    ser.write(command.encode())  # Send command
    time.sleep(0.1)              # Allow time for response
    response = ser.readline().decode().strip() # Read and decode response
    return response

# Main Loop
try:
    while True:
        response = send_and_receive("GET_STATUS") # Replace with the actual command
        
        # Data Interpretation (Example for a simple ON/OFF response)
        if response == "ON":
            print("Methane Detected")
        elif response == "OFF":
            print("No Methane Detected")
        else:
            print("Unknown response:", response)  # Handle unexpected responses

        time.sleep(1)  # Adjust polling interval as needed

except KeyboardInterrupt:
    ser.close()
    print("Program terminated.")
