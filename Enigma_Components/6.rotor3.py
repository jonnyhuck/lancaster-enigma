"""
This script is for the 'rotor' microbits (red #6-8)
It replaces each character and then advances, meaning that the same character will be encrytpted differently next time
There can be as many of these as you like in the system

You need to set `my_id` and `r_to` prior to use
"""

import radio
from microbit import display, sleep


def apply_encryption(msg, forward, r_to):
    """
    Apply the encryption step associated with this component
    """
    # loop through each character in the message
    out = ""
    for counter, char in enumerate(msg):

        # advance the rotor one position (once per revolution of rotor 2)
        if counter % (len(r_to)**2) == 0:
            r_to = advance_rotor(r_to)

        # run forwards through the rotor (ignore characters not in the rotor)
        if forward:
            out += r_to[r_from.index(char)] if char in r_from else char
            
        # run backwards through the rotor (ignore characters not in the rotor)
        else:
            out += r_from[r_to.index(char)] if char in r_to else char
            
    # return the result
    return out, r_to


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

# init rotors
r_from  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
r_bk    = ['E', 'P', 'C', 'Y', 'H', 'J', 'Z', 'G', 'A', 'D', 'X', 'R', 'N', 'F', 'Q', 'S', 'L', 'U', 'V', 'B', 'T', 'K', 'O', 'W', 'M', 'I']
r_to = []

# turn on and configure the radio interface
radio.on()
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
            
            # get forward flag as Boolean value from the message
            forward = msg_components[1] == "True"

            # init / reset the rotor in forward direction only
            if forward:
                r_to = r_bk.copy()

            # apply the encryption step for this device
            encrypted, r_to = apply_encryption(msg_components[2].upper(), forward, r_to)
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()