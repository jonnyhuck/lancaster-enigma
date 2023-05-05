"""
This script is for a 'plugboard' microbit
"""

import radio
from microbit import display, sleep


def apply_encryption(msg):
    """
    THIS FUNCTION NEEDS TO ENCRYPT THE MESSAGE BY SEEING IF THE CHARACTER IN `plug_from` 
    IS IN THE MESSAGE AND SWAPPING IT FOR THE CHARACTER IN `plug_to` (AND VICE VERSA).

    TO MAKE IT EASIER, YOU CAN USE THE VERSION OF `plug_from` and `plug_to` THAT SWAPS 
    ONLY A SINGLE PAIR OF LETTERS. IF YOU WANT MORE OF A CHALLENGE, YOU CAN MAKE `plug_from` 
    and `plug_to` EACH REPRESENT A LIST OF LETTERS AND SWAP ANY LATTER THAT COMES UP WITH 
    THE CORRESPONDING LETTER FROM THE OTHER LIST.
    """
    out = msg
    return out


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
    encrypted = apply_encryption(test_msg.upper())

    # display the result on the screen
    display.scroll(encrypted)


'''
`plug_from` and `plug_to` REPRESENT THE START AND END POINT OF THE PLUG WIRES. 
IF A CHARACTER COMES IN THAT IS IN `plug_from`, YOU WOULD REPLACE IT WITH THE 
CORRESPONDING LETTER IN `plug_to` AND VICE VERSA. YOU EITHER MAKE MICROBIT 
REPRESENT A SINGLE WIRE (BY PUTTING A SINGLE CHARACTER IN EACH VARIABLE) OR 
MULTIPLE (BY PUTTING A LIST IN EACH VARIABLE) - AS LONG AS THERE ARE THE SAME 
NUMBER IN EACH AND EACH CHARACTER APPEARS ONLY ONCE. EXAMPLES OF BOTH ARE GIVEN 
BELOW.
'''

# set the plugs (single characters)
plug_from = 'T'
plug_to   = 'F'

# set the plugs (lists of characters)
# plug_from = ['T', 'R']
# plug_to   = ['F', 'J']

'''
`my_id` SETS THE POSITION OF THIS COMPONENT IN THE ENIGMA MACHINE. YOU DON'T 
NEED TO WORRY ABOUT THIS UNTIL WE JOIN THE MACHINE TOGETHER.
'''

# the id of this device - should denote the devices position in the Enigma
my_id = 2

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

# turn on the radio interface
# radio.on()

# # set radio group
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

#             # apply the encryption step for this device
#             encrypted = apply_encryption(msg_components[2].upper())
            
#             # get forward flag as Boolean value from the message
#             forward = msg_components[1] == "True"
            
#             # work out next destination
#             destination = my_id + 1 if forward else my_id - 1

#             # pass on the message
#             radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
#             display.clear()