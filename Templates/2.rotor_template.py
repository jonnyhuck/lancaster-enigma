"""
* This script is for a 'rotor' microbit
"""

import radio
from microbit import display, sleep


def apply_encryption(msg, forward):
    """
    THIS FUNCTION NEEDS TO ENCRYPT THE MESSAGE BY FINDING ANY CHARACTERS IN `rotor_from`    
    AND SWAPPING THEM WITH THE CORRESPONDING CHARACTER IN `rotor_to` (WHEN `forward` == `True`)
    AND VICE VERSA (when `forward` == `False`).

    TO BE ABLE TO WORK IN BOTH DIRECTIONS, YOU WILL NEED TO 'ADVANCE' THE ROTOR BETWEEN EACH CHARACTER.
    """
    out = msg
    return out


def advance_rotor(rotor, n):
    """
    THIS FUNCTION HANDLES 'ADVANCING' THE ROTOR - IT EFFECTIVELY MOVES THE 'WIRING' THAT DEFINES THE 
    RELATIONSHIP BETWEEN THE LETTER ON EITHJER SIDE OF THE ROTOR.

    AT EACH ADVANCE, THE NEW VALUE FOR A CHARACTER WOULD BE THE SAME NUMBER OF POSITIONS IN THE ALPHABET 
    AWAY FROM IT AS THE DISTANCE BETWEEN THE CHARACTER BEFORE IT IN `r_from` AND ITS COUNTERPART IN `r_to`. 
    THIS GIVES THE EFFECT OF THE WIRING BETWEEN `r_from` and `r_to` ROTATING ONE PLACE. THIS SEEMS COMPLICATED, 
    BUT IS MORE EASILY DEMONSTRATED WITH AN EXAMPLE:
    
    FOR EXAMPLE, IF THE ROTOR LOOKED LIKE THIS
        A -> D (+3)
        B -> F (+4)
        C -> M (+10)
    THEN AFTER ONE ADVANCE IT WOULD BE:
        A -> K (+10)
        B -> E (+3)
        C -> G (+4)
    """    
    # move the offset between the letters forward 1 place, n times
    for _ in range(n):
        for j in range(len(rotor[1])):
                rotor[1][j] = alphabet[(alphabet.index(rotor[1][j]) + 1) % len(alphabet)]
    return rotor


def build_rotor():
    """
    THIS FUNCTION SETS (OR RESETS) THE ROTORS TO THEIR ORIGINAL POSITION - YOU CAN CHANGE THE `r_to` LIST
    BELOW TO CHANGE THE WIRING OF THE ROTOR - JUST MAKE SURE THAT EACH LETTER IS ONLY IN THERE ONCE!
    """
    r_from  = alphabet.copy()
    r_to = ['K', 'W', 'C', 'S', 'J', 'F', 'R', 'V', 'L', 'E', 'N', 'P', 'I', 
            'O', 'Y', 'M', 'D', 'U', 'A', 'T', 'Z', 'B', 'H', 'X', 'G', 'Q']
    return [r_from, r_to]


def test():
    """
    THIS FUNCTION JUST LETS YOU TEST YOUR `apply_encryption()` FUNCTION - IT
    SENDS A MESSAGE TO BE ENCRYPTED AND WRITES THE RESULT TO THE DISPLAY ASIDE 
    FROM EDITING THE TEST MESSAGE IF YOU WISH, YOU SHOULDN'T NEED TO DO ANYTHING 
    TO THIS FUNCTION.
    """
    # test message (you can set this to whatever you like)
    test_msg = "a test message"

    # encrypt the message using your function (above)
    encrypted = apply_encryption(test_msg.upper(), True)

    '''
    NOTE THAT THE MESSAGE WILL ULTIMATELY NEED TO PASS THROUGH THIS ROTOR TWICE.
    ONCE YOU HAVE IMPLEMENTED THE ROTOR ADVANCE BETWEEN EACH CHARACTER - YOU MIGHT 
    WANT TO UN-COMMENT THIS LINE SO THAT YOU CAN TEST IN BOTH DIRECTIONS. (IF YOU 
    DO THIS BEFORE YOU ADD IN ADVANCEMENT THEN IT WILL JUST DECIPHER THE CHARACTER 
    AGAIN)
    '''
    # encrypted = apply_encryption(encrypted, False)

    # display the result on the screen
    display.scroll(encrypted)


'''
`my_id` SETS THE POSITION OF THIS COMPONENT IN THE ENIGMA MACHINE. YOU DON'T 
NEED TO WORRY ABOUT THIS UNTIL WE JOIN THE MACHINE TOGETHER.
'''

# the id of this device - should denote the devices position in the Enigma
my_id = 4


'''
THIS DEFINES THE ALPHABET - IT IS USED IN THE CONSTRUCTION OF THE ROTOR
'''
alphabet  = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


'''
BELOW HERE IS THE CODE TO RECEIVE THE DATA PACKET, READ IT, PASS IT TO 
THE `apply_encryption()` FUNCTION AND SEND IT OFF AGAIN. FEEL FREE TO 
HAVE A LOOK, BUT YOU SHOULDN'T NEED TO EDIT IT. WE WILL LEAVE IT COMMENTED 
OUT UNTIL WE WANT TO USE IT AS OTHERWISE THE MICROBITS MIGHT START 
INTERFERING WITH EACH OTHER WHILE WE ARE WORKING.

WHEN WE COME TO JOIN THE MACHINE TOGETHER, WE WILL WANT TO REMOVE THE `test()`
LINE AND UN-COMMENT THE REST TO REPLACE IT.
'''

test()

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

#             # apply the encryption step for this device
#             encrypted = apply_encryption(msg_components[2].upper(), forward)
            
#             # work out next destination
#             destination = my_id + 1 if forward else my_id - 1

#             # pass on the message
#             radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
#             display.clear()