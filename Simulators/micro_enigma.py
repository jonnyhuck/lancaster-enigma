from microbit import uart
from random import seed, randint

# initialise serial comms
uart.init(baudrate=19200)

# init alphabet list
alphabet  = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def shuffle(list_to_shuffle):
    """
    implementation of Fisher-Yates algorithm
    random.shuffle not available in micropy
    """
    # reverse loop through index of each element in the list
    for i in range(len(list_to_shuffle)-1, 0, -1):
     
        # Pick a random index from 0 to i
        j = randint(0, i + 1)
   
        # swap current element [i] with the element at random index [j]
        list_to_shuffle[i], list_to_shuffle[j] = list_to_shuffle[j], list_to_shuffle[i]
     
    # return shuffled list
    return list_to_shuffle


def build_rotor():
    """
    Construct a new rotor
    """
    # take a plain alphabet
    r_from = alphabet.copy()

    # take a shuffled alphabet
    r_to = shuffle(alphabet.copy())

    # load into list and return
    return [r_from, r_to]


def build_reflector():
    """
    Construct a new rotor
    """
    # shuffle alphabet
    reflector = shuffle(alphabet.copy())

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
        for j in range(len(rotor[1])):
                rotor[1][j] = alphabet[(alphabet.index(rotor[1][j]) + 1) % len(alphabet)]
                
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


# infinite loop
while True:
    
    # try to read a line of serial
    msg = uart.readline()
    
    # if there is a message
    if msg != None:
        
        # convert the message from bytes to string
        msg_str = str(msg, 'UTF-8')
        
        # initialise the enigma
        init()  # just accept default settings

        # run the message through the enigma
        out = run_string(msg_str)
        
        # write the result to serial
        uart.write(out)