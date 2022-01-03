"""
A simple demo of reading and writing between a Raspberry Pi and BBC Microbit over USB.
    This script is for the BBC Microbit. Should be used alongside serial.py on the Raspberry Pi.

@author jonnyhuck
"""
from microbit import uart, display

# initialise serial comms
uart.init(baudrate=19200)

# infinite loop
while True:
    
    # try to read a line of serial
    msg = uart.readline()
    
    # if there is a message
    if msg != None:
        
        # write it to the screen
        display.scroll(msg)
        
        # respond to confirm that the message was received
        uart.write('message received')