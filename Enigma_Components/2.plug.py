"""
This script is for the 'plugboard' microbits (green #2-5)
It represents a single set of plugs on the plugboard that redirects one character to another and vice versa
There can be as many of these as you like in the system

You need to set `my_id`, `plug_from` and `plug_to` before use.
"""

import radio
from microbit import display


def apply_encryption(msg):
    """
    Apply the encryption step associated with this component

    This is a plug in the plugboard, so replace any instance of either the `plug_from` or `plug_to` 
        character with its counterpart
    """

    # loop through each character in the message
    for char in msg:
        
        # swap it if/as required
        if char == plug_from:
            out += plug_to
        elif char == plug_to:
            out += plug_from
        else:
            out += char
    
    # return the result
    return out


# the id of this device - should denote the devices position in the Enigma
my_id = 2
display.show(str(my_id))

# set the plugs
plug_from = 'R'
plug_to   = 'J'

# set radio group (has to be the same for all components)
radio.config(group=41)

# turn on the radio interface
radio.on()

# infinite loop
while True:

    # try to read a message
    packet = radio.receive()
    if packet:
        
        # extract the id, forwards flag and message itself
        msg_components = packet.split("|")

        # if the message is for me
        if int(msg_components[0]) == my_id:

            # apply the encryption step for this device
            msg = apply_encryption(msg_components[2])
            
            # get forward flag as Boolean value from the message
            forward = msg_components[1] == "True"
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1
            
            # pass on the message
            radio.send(str(destination) + "|" + str(forward) + "|" + str(msg))