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
    for char in msg:

        # run forwards through the rotor
        if forward:
            out += r_from[r_to.index(char)]
        
        # run backwards through the rotor
        else:
            out += r_to[r_from.index(char)]
        
        # advance the rotor one position
        advance_rotor()
    return out


def advance_rotor(n=1):
    """
    Advance a rotor n positions
    """
    # do it n times
    for _ in range(n):

        # increase each letter one place along the alphabet
        for j in range(len(r_to)):
            r_to[j] = r_from[(r_from.index(r_to[j]) + 1) % len(r_from)]


# the id of this device - should denote the devices position in the Enigma
my_id = 6
display.show(str(my_id))

# init rotors
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