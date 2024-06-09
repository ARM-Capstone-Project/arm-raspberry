import usb.core
import usb.util

# Replace with your device's actual VID and PID from lsusb
VID = 0x0856  # Vendor ID as a hexadecimal integer
PID = 0xac11  # Product ID as a hexadecimal integer

# Find the device
device = usb.core.find(idVendor=VID, idProduct=PID)
if device is None:
    raise ValueError('Device not found. Check VID/PID and ensure the device is connected.')

# Detach kernel driver if necessary
if device.is_kernel_driver_active(0):
    device.detach_kernel_driver(0)

# Set the active configuration. With no arguments, the first configuration will be the active one.
device.set_configuration()

# Claim the device
usb.util.claim_interface(device, 0)

# Set up communication (modify based on sensor's documentation)
endpoint_in = device[0][(0,0)][0]

# Continuously read and interpret data
while True:
    try:
        # Read data from the endpoint
        data = device.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize)
        
        # Interpret data based on sensor's documentation
        # Example: data[0] might be the status byte
        if data[0] == 0x01:
            print("Methane Detected")
            print(data)
        elif data[0] == 0x00:
            print("No Methane Detected")
        
    except usb.core.USBError as e:
        if e.errno == 110:  # Operation timed out
            continue # Retry if timeout occurs
        else:
            raise e  # Re-raise other USB errors
    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit the loop if a non-USB error occurs

# Release the device
usb.util.release_interface(device, 0)
device.attach_kernel_driver(0)
