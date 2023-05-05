"""
This script is for the 'rotor' microbits (red #6-8)
It replaces each character and then advances, meaning that the same character will be encrytpted differently next time
"""

import radio
from microbit import display, sleep


def apply_encryption(msg, forward, rotor):
    """
    Apply the encryption step associated with this component
    """
    # loop through each character in the message
    out = ""
    for count, char in enumerate(msg):

        # get the character number for this message
        n = count + 1

        # put the rotor back to the start
        rotor = build_rotor()

        # advance the rotor the correct number of positions (once per revolution of rotor 1)
        if n % len(alphabet) == 0:
            rotor = advance_rotor(rotor, n // len(alphabet))

        # run forwards through the rotor (ignore characters not in the rotor)
        if forward:
            out += rotor[1][rotor[0].index(char)] if char in rotor[0] else char
            
        # run backwards through the rotor (ignore characters not in the rotor)
        else:
            out += rotor[0][rotor[1].index(char)] if char in rotor[1] else char
            
    # return the result
    return out, rotor


def advance_rotor(rotor, n):
    """
    Advance a rotor n positions
    """
    # move the offset between the letters forward 1 place, n times
    for _ in range(n):
        for j in range(len(rotor[1])):
                rotor[1][j] = alphabet[(alphabet.index(rotor[1][j]) + 1) % len(alphabet)]
    return rotor


def build_rotor():
    """
    Initialise / Reset a new rotor
    """
    r_from  = alphabet.copy()
    r_to = ['Z', 'W', 'F', 'R', 'U', 'I', 'C', 'M', 'X', 'S', 'Q', 'O', 'P', 
            'E', 'G', 'A', 'T', 'B', 'H', 'L', 'Y', 'V', 'K', 'N', 'D', 'J']
    return [r_from, r_to]


# the id of this device - should denote the devices position in the Enigma
my_id = 5

# setup for rotor
alphabet  = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rotor = []

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

            # apply the encryption step for this device
            encrypted, rotor = apply_encryption(msg_components[2].upper(), forward, rotor)
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()