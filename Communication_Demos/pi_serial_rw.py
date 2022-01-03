"""
A simple demo of reading and writing between a Raspberry Pi and BBC Microbit over USB.
    This script is for the Raspberry Pi. Should be used alongside microbit_serial.py on the
    BBC Microbit.

@author jonnyhuck
"""
from serial import Serial
from os import path, listdir

# this is the location of the serial devices list
serial_dev_dir = '/dev/serial/by-id'

# verify it exists
if path.isdir(serial_dev_dir):

    # get the list of serial devices
    serial_devices = listdir(serial_dev_dir)

    # make sure that at least one device is available
    if len(serial_devices) > 0:

        # get the path to the first available device
        serial_device_path = path.join(serial_dev_dir, serial_devices[0])

        # open serial interface
        serial = Serial(port=serial_device_path, baudrate=19200, timeout=0.5)

        # write something
        serial.write(bytes(b'Hello World'))
    
    else:
        print("No serial device available")
        exit(1)
else:
    print("No serial device connected")
    exit(1)

# infinite loop
while True:

    # try to read from the serial interface
    msg = serial.readline()

    # wait for a message to come back
    if len(msg) > 0:

        # convert to string and print
        print(msg.decode('utf-8'))

        # exit the infinite loop
        break