import serial

RS485 = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


try:
    print("try!!!")
    while True:
        x = RS485.readline()
        print(x)

except KeyboardInterrupt:
    print("except!!!")
    ser.close()

