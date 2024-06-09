import usb.core
import usb.util

# Replace with your device's actual VID and PID from lsusb
VID = 0x0856  # Vendor ID as a hexadecimal integer
PID = 0xac11  # Product ID as a hexadecimal integer

# Find the device
device = usb.core.find(idVendor=VID, idProduct=PID)
if device is None:
    raise ValueError('Device not found. Check VID/PID and ensure the device is connected.')


# Set up communication (modify based on sensor's documentation)
endpoint_in = device[0][(0,0)][0]

print(endpoint_in)

# Continuously read and interpret data
while True:
    try:
        
        data = device.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize)
        
        # Interpret data based on sensor's documentation
        # Example: data[0] might be the status byte
        
        if data[0] == 0x01:
            print("Methane Detected")
            print(data[0])
        elif data[0] == 0x00:
            print("No Methane Detected")
        
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue # Retry if timeout occurs
# Set up communication (modify based on sensor's documentation)
endpoint_in = device[0][(0,0)][0]

# Continuously read and interpret data
while True:
    try:
        data = device.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize)
        
        # Interpret data based on sensor's documentation
        # Example: data[0] might be the status byte
        if data[0] == 0x01:
            print("Methane Detected")
        elif data[0] == 0x00:
            print("No Methane Detected")
        
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue # Retry if timeout occurs