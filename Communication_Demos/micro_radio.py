'''
Simple demo of how to pass messages between BBC Microbits using the built in 
    radio interface.

Messages are in the form:
    target_id|forward|message
e.g.: 
    3|True|Hello World
    
@author jonnyhuck
'''
import radio
from microbit import display, sleep, button_a

# the id of this device - should denote the devices position in the Enigma
my_id = 1

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
            display.show(str(my_id))

            # wait 1 second
            sleep(1000)
            
            # get forward flag as Boolean value from the message
            forward = msg_components[1] == "True"
            
            # flip forward flag for reflectors
            if my_id in [1, 3]: 
                forward = not forward
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1
            
            # pass on the message
            radio.send(str(destination) + "|"+ str(forward) +"|" + "Test")
            display.clear()
    
    # also send a message if button a is pressed
    if button_a.was_pressed():
        radio.send("2|True|Test")
        display.clear()