"""
This script is for the 'plugboard' microbits (green #2-5)
It represents a single set of plugs on the plugboard that redirects one character to another and vice versa

You need to set `plug_from` and `plug_to` before use.
"""

import radio
from microbit import display, sleep


def apply_encryption(msg):
    """
    Apply the encryption step associated with this component

    This is a plug in the plugboard, so replace any instance of either the `plug_from` or `plug_to` 
        character with its counterpart
    """

    # loop through each character in the message, swap it if/as required
    global plug_from, plug_to
    out = ""
    for char in msg:
        if char == plug_from:
            out += plug_to
        elif char == plug_to:
            out += plug_from
        else:
            out += char
    return out


# the id of this device - should denote the devices position in the Enigma
my_id = 3

# set the plugs
global plug_from, plug_to
plug_from = 'J'
plug_to   = 'R'

# turn on the radio interface
radio.on()

# set radio group
radio.config(group=1)

# infinite loop
while True:

    # try to read a message
    packet = radio.receive()
    if packet:
        
        # extract the id, forwards flag and message itself
        msg_components = packet.split("|")

        # if the message is for me
        if int(msg_components[0]) == my_id:
            display.show(str(my_id))
            sleep(int(msg_components[3]))

            # apply the encryption step for this device
            encrypted = apply_encryption(msg_components[2].upper())
            
            # get forward flag as Boolean value from the message
            forward = msg_components[1] == "True"
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()