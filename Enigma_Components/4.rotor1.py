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
    for char in msg:

        # advance the rotor one position (once per character)
        # rotor = advance_rotor(rotor)

        # run forwards through the rotor (ignore characters not in the rotor)
        if forward:
            out += rotor[1][rotor[0].index(char)] if char in rotor[0] else char
            
        # run backwards through the rotor (ignore characters not in the rotor)
        else:
            out += rotor[0][rotor[1].index(char)] if char in rotor[1] else char
            
    # return the result
    return out, rotor


def advance_rotor(rotor, n=1):
    """
    Advance a rotor n positions
    """
    # increase each letter one place along the alphabet, n times
    for _ in range(n):
        for j in range(len(rotor[1])):
                rotor[1][j] = alphabet[(alphabet.index(rotor[1][j]) + 1) % len(alphabet)]
    return rotor


def build_rotor():
    """
    Initialise / Reset a new rotor
    """
    r_from  = alphabet.copy()
    r_to = ['K', 'W', 'C', 'S', 'J', 'F', 'R', 'V', 'L', 'E', 'N', 'P', 'I', 
            'O', 'Y', 'M', 'D', 'U', 'A', 'T', 'Z', 'B', 'H', 'X', 'G', 'Q']
    return [r_from, r_to]


# the id of this device - should denote the devices position in the Enigma
my_id = 4

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

            # init / reset the rotor in forward direction only
            if forward:
                rotor = build_rotor()

            # apply the encryption step for this device
            encrypted, rotor = apply_encryption(msg_components[2].upper(), forward, rotor)
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()


# def init():
#     """
#     Initialise / re-initialise to original settings
#     """
#     # reset counter
#     global counter
#     counter = 1

#     # build rotor
#     global r1
#     r1 = build_rotor()


# def build_rotor():
#     """
#     Initialise / Reset a new rotor
#     """
#     # rebuld rotor
#     r_from  = alphabet.copy()
#     r_to = ['K', 'W', 'C', 'S', 'J', 'F', 'R', 'V', 'L', 'E', 'N', 'P', 'I', 
#             'O', 'Y', 'M', 'D', 'U', 'A', 'T', 'Z', 'B', 'H', 'X', 'G', 'Q']
#     return [r_from, r_to]


# def apply_encryption(string_in, forward):
#     """
#     Convenience function to run a string
#     """
#     # run each character, assemble into string and return
#     return ''.join([run(char, forward) for char in string_in])


# def run(char, forward):
#     """
#     Run a single character through the enigma machine
#     Rejects anything that isn't a letter or space 
#     """
#     # set to upper case
#     char = char.upper()
	
#     # ignore characters not in alphabet (but leave spaces)
#     if char not in alphabet:
#         if char == ' ':
#             return char
#         else:
#             return ''

#     # advance rotors (happens before enciphering)
#     global r1
#     r1 = advance_rotor(r1)

#     # rotor 1
#     char = run_rotor(r1, char, forward)

#     # increment counter
#     global counter
#     counter += 1

#     # return character
#     return char


# def advance_rotor(rotor, n=1):
#     """
#     Advance a rotor n positions
#     """
#     # do it n times
#     for _ in range(n):

#         # increase each letter one place along the alphabet
#         for j in range(len(rotor[1])):
#                 rotor[1][j] = alphabet[(alphabet.index(rotor[1][j]) + 1) % len(alphabet)]
                
#     # return the resulting rotor
#     return rotor


# def run_rotor(r, char, forward):
#     """
#     Run a character through a rotor
#     """
#     # run forwards through the rotor
#     if forward:
#         return r[1][r[0].index(char)]
    
#     # run backwards through the rotor
#     else:
#         return r[0][r[1].index(char)]


# # the id of this device - should denote the devices position in the Enigma
# my_id = 4

# # setup for rotor
# alphabet  = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# # turn on and configure the radio interface
# radio.on()
# radio.config(group=1)

# # infinite loop
# while True:

#     # try to read a message
#     packet = radio.receive()
#     if packet:
        
#         # extract the id, forwards flag and message itself
#         msg_components = packet.split("|")

#         # if the message is for me
#         if int(msg_components[0]) == my_id:
#             display.show(str(my_id))
#             sleep(int(msg_components[3]))
            
#             # get forward flag as Boolean value from the message
#             forward = msg_components[1] == "True"

#             # init / reset the rotor in forward direction only
#             if forward:
#                 init()

#             # apply the encryption step for this device
#             encrypted = apply_encryption(msg_components[2], forward)
            
#             # work out next destination
#             destination = my_id + 1 if forward else my_id - 1

#             # pass on the message
#             radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
#             display.clear()