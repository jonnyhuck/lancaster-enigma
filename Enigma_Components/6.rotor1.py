"""
This script is for the 'rotor' microbits (red #6-8)
It replaces each character and then advances, meaning that the same character will be encrytpted differently next time
There can be as many of these as you like in the system

You need to set `my_id` and `r_to` prior to use
"""

import radio
from microbit import display


def apply_encryption(msg, forward):
    """
    Apply the encryptionstep associated with this component
    """

    # loop through each character in the message
    out = ""
    global r_to
    for char in msg:

        # advance the rotor one position
        r_to = advance_rotor(r_to)

        # we are only encrypting letters at the moment - anything else goes straight back
        if char not in r_from:
            out += char

        # run forwards through the rotor
        elif forward:
            out += r_to[r_from.index(char)]
        
        # run backwards through the rotor
        else:
            out += r_from[r_to.index(char)]
    
    # return the result
    return out


def advance_rotor(rotor, n=1):
    """
    Advance a rotor n positions
    """
    # move each letter one place along the alphabet n times
    for _ in range(n):
        for j in range(len(rotor[1])):
            rotor[j] = r_from[(r_from.index(rotor[j]) + 1) % len(r_from)]
    return rotor


# the id of this device - should denote the devices position in the Enigma
my_id = 6
display.show(str(my_id))

# init rotors
global r_to
r_from  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
r_to    = ['K', 'W', 'C', 'S', 'J', 'F', 'R', 'V', 'L', 'E', 'N', 'P', 'I', 'O', 'Y', 'M', 'D', 'U', 'A', 'T', 'Z', 'B', 'H', 'X', 'G', 'Q']

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
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1
            
            # pass on the message
            radio.send(str(destination) + "|" + str(forward) + "|" + str(msg))