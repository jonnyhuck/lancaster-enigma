"""
This script is for the 'reflector' microbit (yellow #9)
It is like a rotor, but also reverses the `forward` flag and is only run once (everything else runs twice)

This should have the highest `my_id` number in the system
"""

import radio
from microbit import display, sleep


def apply_encryption(msg):
    """
    Apply the encryption step associated with this component
    """
    # loop through each character in the message
    out = ""
    for char in msg:

        # run through the reflector (r1->r2)
        if char in r1:
            out += r2[r1.index(char)]

        # run through the reflector (r2->r1)
        elif char in r2:
            out += r1[r2.index(char)]

        # we are only encrypting letters at the moment - anything else goes straight back
        else:
            out += char

    # return the result
    return out


# the id of this device - should denote the devices position in the Enigma
my_id = 7

# init reflector (13 matched pairs)
r1 = ['R', 'K', 'U', 'Q', 'H', 'I', 'F', 'G', 'D', 'V', 'M', 'W', 'A']
r2 = ['Y', 'Z', 'O', 'B', 'S', 'J', 'C', 'P', 'N', 'X', 'E', 'T', 'L']

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

            # reverse direction
            forward = not forward
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()
            