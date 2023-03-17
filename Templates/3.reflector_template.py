"""
* This script is for the 'reflector' microbit
"""

import radio
from microbit import display, sleep


def apply_encryption(msg):
    """
    THIS FUNCTION NEEDS TO ENCRYPT THE MESSAGE BY FINDING ANY LETTERS IN `r1` 
    AND SWAPPING THEM WITH THE CORRESPONDING LETTERS IN `r2`, AND VICE-VERSA
    """
    # return the result
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
r1 and r2 REFLECT THE WIRING OF THE REFLECTOR - IF A CHARACTER COMES IN 
THAT IS IN `r1`, YOU WOULD REPLACE IT WITH THE CORRESPONDING LETTER IN 
`r2` AND VICE VERSA. YOU CAN SET THE CHARACTERS UP ANY WAY THAT YOU LIKE 
AS LONG AS THERE ARE THE SAME NUMBER IN EACH AND EACH CHARACTER APPEARS 
ONLY ONCE
'''

# init reflector (13 matched pairs)
r1 = ['R', 'K', 'U', 'Q', 'H', 'I', 'F', 'G', 'D', 'V', 'M', 'W', 'A']
r2 = ['Y', 'Z', 'O', 'B', 'S', 'J', 'C', 'P', 'N', 'X', 'E', 'T', 'L']


'''
`my_id` SETS THE POSITION OF THIS COMPONENT IN THE ENIGMA MACHINE. YOU DON'T 
NEED TO WORRY ABOUT THIS UNTIL WE JOIN THE MACHINE TOGETHER, BUT WHEN WE DO 
THIS SHOULD BE THE HIUGHEST NUMBER IN THE WHOLE SYSTEM.
'''

# the id of this device - should denote the devices position in the Enigma
my_id = 7

'''
BELOW HERE IS THE CODE TO RECEIVE THE DATA PACKET, READ IT, PASS IT TO 
THE `apply_encryption()` FUNCTION AND SEND IT OFF AGAIN. FEEL FREE TO 
HAVE A LOOK, BUT YOU SHOULDN'T NEED TO EDIT IT. WE WILL LEAVE IT COMMENTED 
OUT UNTIL WE WANT TO USE IT AS OTHERWISE THE MICROBITS MIGHT START 
INTERFERING WITH EACH OTHER WHILE WE ARE WORKING.

WHEN WE COME TO JOIN THE MACHINE TOGETHER, WE WILL WANT TO REMOVE THE `test()`
LINE AND UN-COMMENT THE REST TO REPLACE IT.
'''

# run the test function
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

#             # reverse direction
#             forward = not forward
            
#             # work out next destination
#             destination = my_id + 1 if forward else my_id - 1

#             # pass on the message
#             radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
#             display.clear()
            