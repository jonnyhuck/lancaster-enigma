"""
This script is for the 'io' microbit (blue #1)
It handles reading and writing between the Raspberry PI (via serial) and the Microbits (via radio)
There can only be one of these in the system

No setup is required - this should always be `my_id` = 1

TODO: This must be run on one of the older microbits (with shiny surface) - the new ones (with matt 
    surface) give a Unicode Error because an empty bytestring is returned. This is probably just down 
    to a different spec, but needs investigating.

TODO: Need to implement a buffering operation to make sure we get the full string
"""

import radio
from microbit import uart, display, sleep

# initialise serial comms
uart.init(baudrate=19200)

# the id of this device - should denote the devices position in the Enigma
my_id = 1

# turn on the radio interface
radio.on()

# set radio group
radio.config(group=1)

# init variables for bodge
counter = 0
message1 = ""
delay = 1000

# infinite loop
while True:

    ''' SERIAL -> RADIO '''

    # try to read a line of serial
    msg = uart.readline()
    
    # if there is a message
    if msg != None:

        # get the first half
        if counter == 0:
            display.show(str(my_id))
            message1 = str(msg.upper(), 'UTF-8')
            counter+=1

        # convert the message from bytes to string and pass on the message via radio
        else:
            sleep(delay)
            radio.send("|".join([str(my_id + 1), str(True), message1 + str(msg.upper(), 'UTF-8'), str(delay)]))
            counter-=1
            display.clear()
        
    ''' RADIO -> SERIAL'''

    # try to read a message
    packet = radio.receive()
    if packet:
        
        # extract the id, forwards flag and message itself
        msg_components = packet.split("|")

        # if the message is for me
        if int(msg_components[0]) == my_id:
            display.show(str(my_id))
            sleep(int(msg_components[3]))
            
            # write the result direct to serial
            uart.write(msg_components[2])
            display.clear()