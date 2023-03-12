"""
This script is for the 'reflector' microbit (yellow #9)
It is like a rotor, but also reverses the `forward` flag and is only run once (everything else runs twice)
There can only be one of these in the system

You need to set `my_id` (should be the highest number in the system) and `r_to` prior to use
"""

import radio
from microbit import display


def apply_encryption(msg):
    """
    Apply the encryptionstep associated with this component
    """
    # loop through each character in the message
    out = ""
    for char in msg:

        # run forwards through the rotor
        if char in r1:
            out += r1[r2.index(char)]
        
        # run backwards through the rotor
        else:
            out += r2[r1.index(char)]
    return out


# the id of this device - should denote the devices position in the Enigma
my_id = 9
display.show(str(my_id))

# init reflector (13 matched pairs)
r1 = ['R', 'K', 'U', 'Q', 'H', 'I', 'F', 'G', 'D', 'V', 'M', 'W', 'A']
r2 = ['Y', 'Z', 'O', 'B', 'S', 'J', 'C', 'P', 'N', 'X', 'E', 'T', 'L']

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
            
            # get forward flag as Boolean value from the message
            forward = msg_components[1] == "True"

            # apply the encryption step for this device
            msg = apply_encryption(msg_components[2], forward)
            
            # flip forward flag (as it is the reflector)
            forward = False
            
            # pass on the message
            radio.send(str(my_id - 1) + "|" + str(forward) + "|" + str(msg))