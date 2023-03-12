"""
This script is for the 'io' microbit (blue #1)
It handles reading and writing between the Raspberry PI (via serial) and the Microbits (via radio)
There can only be one of these in the system

No setup is required - this should always be `my_id` = 1
"""

import radio
from microbit import uart, display

# initialise serial comms
uart.init(baudrate=19200)

# the id of this device - should denote the devices position in the Enigma
my_id = 1
display.show(str(my_id))

# set radio group (has to be the same for all components)
radio.config(group=41)

# turn on the radio interface
radio.on()

# infinite loop
while True:

    ''' SERIAL -> RADIO '''

    # try to read a line of serial
    msg = uart.readline()
    
    # if there is a message
    if msg != None:
        
        # convert the message from bytes to string and pass on the message via radio
        radio.send(str(2) + "|True|" + str(msg, 'UTF-8'))
        

    ''' RADIO -> SERIAL'''

    # try to read a message
    packet = radio.receive()
    
    # if there is a message
    if packet:
        
        # extract the id, forwards flag and message itself
        msg_components = packet.split("|")

        # if the message is for me
        if int(msg_components[0]) == my_id:
            
            # write the result direct to serial
            uart.write(msg_components[2])