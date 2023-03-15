"""
This script is for the 'reflector' microbit (yellow #9)
It is like a rotor, but also reverses the `forward` flag and is only run once (everything else runs twice)
There can only be one of these in the system

You need to set `my_id` (should be the highest number in the system) and `r_to` prior to use
"""

import radio
from microbit import display, sleep


def apply_encryption(msg):
    """
    Apply the encryptionstep associated with this component
    """
    # loop through each character in the message
    out = ""
    for char in msg:

        # we are only encrypting letters at the moment - anything else goes straight back
        if char not in (r1 + r2):
            out += char

        # run forwards through the rotor
        elif char in r1:
            out += r2[r1.index(char)]
        
        # run backwards through the rotor
        else:
            out += r1[r2.index(char)]

    # return the result
    return out


# the id of this device - should denote the devices position in the Enigma
my_id = 4

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
            