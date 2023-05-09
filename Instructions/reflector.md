# # Making a Reflector

First, open the MicroBit Python editor by clicking [here](https://python.microbit.org/v/3), clear all of the code that is in there and and paste in the below code instead - this is a template to get you started:

```python
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
```

Run this code, it should write `A TEST MESSAGE` to the display of your microbit. now see if you can work out how to change the message to something of your own and test it again to make sure that it works. 

## The reflector cipher

The job of the reflector is simply to scramble the characters in the incoming message. Like the rotors,  every character is wired to another character, which is used as a replacement for the original. However, unlike the rotors, which have 26 pairs characters wired to each other, the reflector only has 13 pairs. The reflector also does not advance like a rotor. You could therefore think of it as a plug-board with 13 plugs, meaning that every letter in the alphabet was connected to another letter. 

This wiring is represented in your code by two **lists** of characters, each character in `r1` is wired to the character in the same position in `r2` (i.e., if your message contained a `R`, it would be enciphered to a `Y`; `H` to `S`, and so on):

```python
# init reflector (13 matched pairs)
r1 = ['R', 'K', 'U', 'Q', 'H', 'I', 'F', 'G', 'D', 'V', 'M', 'W', 'A']
r2 = ['Y', 'Z', 'O', 'B', 'S', 'J', 'C', 'P', 'N', 'X', 'E', 'T', 'L']
```

Your job is therefore simply to swap each latter in `r1` for its counterpart in the `r2`. 

## Some coding basics

To make this happen in Python, you need to edit the `def apply_encryption(msg):` **function**. A **function** is simply a block of code that does something, and is created using a `def` (define) statement, after everything inside the function should be **indented** underneath the `def` statement. You can see this in the function as it is at the moment:

```python
def apply_encryption(msg):
    """
    THIS FUNCTION NEEDS TO ENCRYPT THE MESSAGE BY SEEING IF THE CHARACTER IN `plug_from` 
    IS IN THE MESSAGE AND SWAPPING IT FOR THE CHARACTER IN `plug_to` (AND VICE VERSA).

    TO MAKE IT EASIER, YOU CAN USE THE VERSION OF `plug_from` and `plug_to` THAT SWAPS 
    ONLY A SINGLE PAIR OF LETTERS. IF YOU WANT MORE OF A CHALLENGE, YOU CAN MAKE `plug_from` 
    and `plug_to` EACH REPRESENT A LIST OF LETTERS AND SWAP ANY LATTER THAT COMES UP WITH 
    THE CORRESPONDING LETTER FROM THE OTHER LIST.
    """
    out = msg 	# this line is indented with a tab from the left
    return out	# so is this
```

The text between the `"""` symbols and after the `#` symbol are **comments**, these are to tell you what is going on in the code, and are simply ignored by the computer. The two lines of code in the function are **indented** (have a tab to the left of them) to show that they are inside the **function**. 

`out` is a **variable** - this simply stores a value. In this case, we are storing a copy of the contents of `msg` into the `out` **variable** using the assigmne t operator (`=`).

**Functions** typically take in one or more values as **arguments** (this one has one argument called `msg`, which is the message we want to encrypt), does something to them, and then **returns** a new value using a `return` statement. For example, the below function takes in an **argument**, multiplies it by 2, and then **returns** it:

```python
def double(number):

  # double the number and store it in a variable called `out`
  out = number * 2
  
  # return the doubled number
  return out
```

I can then **call** the function like this...

```python
result = double(2)
```

...which would mean that the value `4` would be **returned** and stored in the `result` **variable**. 

## Making the reflector

In our case, we want our `apply_encryption` **function** to take in one **argument** called `msg`, which contains our message to encrypt, apply our reflector encryption, and then **return** the encrypted text. Your job is simply to fill in the code for the function to apply the encryption. Here is what we need it to do:

1. Look at every character in the incoming message in turn
3. If it is the character in `r1`, switch it for the character in `r2`
4. If it is the character in `r2`, switch it for the character in `r1`
5. Otherwise, just keep the original character

Let's go...

### Step 1: Looking at every character

Currently, our function is simply copying the incoming message (`msg`) into the **variable**  `out`, which gets returned, so it simply returns the same message that we started with. Clearly this is not what we want, so change this line:

```python
out = msg
```

To this:

```python
out = ""
```

This means that out is now an empty block of text. We can now add our encrypted characters to it one by one until we are finished.

In Python, we call a block of text a **String** of **characters** - Python cannot read, so it doesn't see words, simply lists of letters (which it calls **characters**). We access items in a list using square brackets and an **index** number, which is simply the position of the character in the list, starting at `0`. The first letter in a message is therefore in position `0`, the second in position `1`, and so on. Here is an example:

```python
message = "Hi Mum"

print(message[0]) 
H

print(message[4]) 
u
```

If, rather than accesseach item in the  **list** individually, we would like to systematically look through each elementin turn, we use a `for` **loop**, which is a bit of code that repeats once for each item in a **list**. Here is how it works:

```python
for char in msg:	
  out += char
```

As you can see, inside the `for` loop is another indented block - this runs once per **item** in the **list** (character in the message in our case). Here, it is adding (`+=`) the current character (`char`) to the end of our new message - which will simply  duplicate the original message.

Add the above to your code below `out = ""` but above `return out`, making sure that it is indented (the second line also needs to be indented a second time, to show that it is inside the `for` **loop**). 

Now run your code. If it works, it should still write the original message to the screen, but now it is doing it by adding each character one by one, rather than all at once. 

### Step 2: Swapping letters and searching lists

The next step is to work out if each character is in `r1` and if so, switch it for the corresponding letter in  `r2`. We can do this with an `if` statement, which is a bit of code that tests whether or not somethign is true, and acts accordingly. For example:

```python
# run through the reflector (r1->r2)
if char in r1:
    out += r2[r1.index(char)]

# we are only encrypting letters at the moment - anything else goes straight back
else:
    out += char
```

The first line in the above snippet checks whether the current character (`char`) is in the **list** `r1`. 

If so, we need to work out what position in the list it is (remember, the first item in the list is position `0`, the second is position `1`, and so on). We can do this with `r1.index(char)`, which is a **function** that **returns** the position (**index** number) of `char` in `r1`. We then pass that to `r2` using square brackets `[ ]` to retrieve the that is in this position. Finally, we append the character from `r2` to `out` (`+=`) instead of the original character, thus encrypting it.

Replace the contents of the `for` **loop** with the above code and then run it. If you have done it correctly, the letters from `r1`should all be replaced with their counterparts from `r2`.

### Step 4. Swapping letters in the other direction

`if` statements can have multiple tests using the `elif` keyword (which means **else if**). You can have as many `elif` statements as you, and an  `elif` will only be tested if all of the `if` and `elif` statements above it are `False`. For example:

```python
my_name = "Mr Huck"

# this will be tested and is false...
if my_name == "Mr Hockey":
  # ...so any code here will NOT run

# this will be tested and is true...
elif my_name == "Mr Huck":
  # ...so any code here will run

# this will NOT be tested because one of the above if/elif statements was true...
elif my_name == "Mr Waddock"
  # ...so any code here will NOT run

# this is NOT needed because one of the above if/elif statements was true...
else:
    # ...so any code here will NOT run
```

Now see if you can add an `elif` condition to the `if` statement to make it swap the letters in the *other* direction (i.e., from `r2` to `r1`). 

If all has gone to plan, when you run your code all of the characters should be replaces with their counterparts from the other list.

## When you are finished

Once you are happy that your code works, you can simply delete the line that says `test()` (the last line), and add the following code to the bottom of your script:

```python
# turn on and configure the radio interface
radio.on()

# set radio group
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
  
            # apply the encryption step for this device
            encrypted = apply_encryption(msg_components[2].upper())

            # get forward flag as Boolean value from the message
            forward = msg_components[1] == "True"

            # reverse direction
            forward = not forward
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()
```

This simply handles the radio communications between the microbits and makes a **call** to your `apply_encryption` **function** - feel free to take a look (see if you can find the function call), but don't worry if you don't fully understand it. 

Once that is done - your microbit is ready to be added to the rest of them to make the enigma machine!