
"""
Enigma machine implemented in Python for Lancaster Air Cadets

This implementation follows the description by Singh (2002). This is intended to be divided up into a series 
    of BBC Microbits for the purpose of building a simple demonstration model of an Enigma machine - it is written 
    with this in mind and to maximise simplicity and readability, rather than efficiency or progrramming best practice.
    In particular, it uses a very simple rotor model, which is randomly generated and does not have a ring setting.

When a character is submitted, it goes through:
 - a plugboard (each wire on the plugboard will be one microbit)
 - three rotors (each rotor will be one microbit)
 - a reflector (one microbit)
 - the three rotors again
 - the plugboard again

 The rotors move on one position, meaning that the same character in plain text will not be encrypted to the 
    given the same character in cipher text. The rotors move:
 - rotor 1 moves every character
 - rotor 2 moves once every full revolution of rotor 1
 - rotor 3 moves once every full revolution of rotor 2

The initial settings of the machine (passed to init) are important, as a message can only be decrypted using the
    identical settings. These are the starting positions of the three rotors and a seed for the random number generator 
    (which we use to generate the rotor wiring) - the latter could be hard-coded to eliminate this setting if preferred.

@author jonnyhuck
@version 0.3
"""

from random import shuffle, seed

# init alphabet list
alphabet  = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def build_rotor():
    """
    Construct a new rotor
    """
    # take a plain alphabet
    r_from = alphabet.copy()

    # take a shuffled alphabet
    r_to = alphabet.copy()
    shuffle(r_to)

    # load into list and return
    return [r_from, r_to]


def build_reflector():
    """
    Construct a new rotor
    """
    # shuffle alphabet
    reflector = alphabet.copy()
    shuffle(reflector)

    # split in half
    r_from = reflector[:13]
    r_to = reflector[13:]

    # load into list and return
    return [r_from, r_to]


def run_plugs(char):
    """
    Run a character through the plugboard
    """
    # test and swap character in both directions
    global plugs_from
    global plugs_to
    if char in plugs_from:
        return plugs_to[plugs_from.index(char)]
    elif char in plugs_to:
        return plugs_from[plugs_to.index(char)]
    else:
        return char


def run_rotor(r, char, forward):
    """
    Run a character through a rotor
    """
    # run forwards through the rotor
    if forward:
        return r[1][r[0].index(char)]
    
    # run backwards through the rotor
    else:
        return r[0][r[1].index(char)]


def run_reflector(r, char):
    """
    Run a character through a reflector
    """
    # test and swap character in both directions
    if char in r[0]:
        return r[1][r[0].index(char)]
    else:
        return r[0][r[1].index(char)]


def advance_rotor(rotor, n=1):
    """
    Advance a rotor n positions
    """
    # do it n times
    for i in range(n):

        # increase each letter one place along the alphabet
        for letter in range(len(rotor[1])):
            rotor[1][letter] = alphabet[(alphabet.index(rotor[1][letter]) + 1) % len(alphabet)]
    
    # return the resulting rotor
    return rotor


def advance_rotors():
    """
    Advance the rotors as required for each character passing through the machine
    """
    # advance rotor 1 every time
    global r1
    r1 = advance_rotor(r1)

    # advance rotor 2 every loop of rotor 1
    global r2
    if counter % len(alphabet) == 0:
        r2 = advance_rotor(r2)
        
    # advance rotor 3 every loop of rotor 2
    global r3
    if counter % (len(alphabet)**2) == 0:
        r3 = advance_rotor(r3)


def init(r1_position=0, r2_position=0, r3_position=0, rng_seed=345, set_plugs_from=['R','C'], set_plugs_to=['J','H']):
    """
    Initialise / re-initialise the enigma machine to original settings
    """
    # set random seed
    seed(rng_seed)

    # set plugs
    global plugs_from
    plugs_from = set_plugs_from
    global plugs_to
    plugs_to = set_plugs_to
    
    # reset counter
    global counter
    counter = 1

    # build rotor 1 and set position
    global r1
    r1 = build_rotor()
    if r1_position > 0:
        r1 = advance_rotor(r1, r1_position)

    # build rotor 2 and set position
    global r2
    r2 = build_rotor()
    if r2_position > 0:
        r2 = advance_rotor(r2, r2_position)

    # build rotor 3 and set position
    global r3
    r3 = build_rotor()
    if r3_position > 0:
        r3 = advance_rotor(r3, r3_position)

    # build reflector
    global reflector
    reflector = build_reflector()


def run(char):
    """
    Run a single character through the enigma machine
    Rejects anything that isn't a letter or space 
    """
    # set to upper case
    char = char.upper()
	
    # ignore characters not in alphabet (but leave spaces)
    if char not in alphabet:
        if char == ' ':
            return char
        else:
            return ''

    # advance rotors (happens before enciphering)
    advance_rotors()

    # apply plugs
    char = run_plugs(char)

    # rotor 1
    char = run_rotor(r1, char, True)

    # rotor 2
    char = run_rotor(r2, char, True)

    # rotor 3
    char = run_rotor(r3, char, True)

    # reflector
    char = run_reflector(reflector, char)

    # rotor 3
    char = run_rotor(r3, char, False)

    # rotor 2
    char = run_rotor(r2, char, False)

    # rotor 1
    char = run_rotor(r1, char, False)

    # apply plugs
    char = run_plugs(char)

    # increment counter
    global counter
    counter += 1

    # return character
    return char


def run_string(string_in):
    """
    Convenience function to run a string
    """
    # run each character, assemble into string and return
    return ''.join([run(char) for char in string_in])


def test(plain="Oooh look, a secret!"):
    """
    Simple test function
    """
    # print plain text
    print("plain:    ", plain)

    # encrypt and print
    init() # just accept default settings
    encrypted = run_string(plain)
    print("encrypted:", encrypted)

    # decrypt and print
    init() # just accept default settings
    print("decrypted:", run_string(encrypted) + "\n")


# if file is executed directly, launch interactive terminal
if __name__ == "__main__":

    # clear the console
    from os import system as os_system
    os_system('clear')

    # start user output
    print(f"\nWelcome to the Lancaster Enigma")
    print(f"Enter '/exit' or '/x', or use Ctrl+C to exit\n")
    print(f"Enter '/test' or '/t'to run a demo\n")

    # infinite loop
    while True:

        # read in message from the user
        string_in = input("Enter message to encrypt / decrypt: ")

        # end on /exit command
        if string_in in ["/exit", "/x"]:
            break

        # run demo on \test command
        if string_in in ["/test", "/t"]:
            test()
        
        # otherwise run the input text
        else:
            # run the message through the enigma
            init()  # just accept default settings
            print(run_string(string_in) + "\n")