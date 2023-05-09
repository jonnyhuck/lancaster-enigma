# # Making a Plug Board

First, open the MicroBit Python editor by clicking [here](https://python.microbit.org/v/3), clear all of the code that is in there and and paste in the below code instead - this is a template to get you started:

```python
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
THIS MAKES THE `test()` FUNCTION (ABOVE) RUN - YOU CAN USE THIS TO SEE IF YOUR 
ENCRYPTION IS WORKING.
'''

test()
```

Run this code, it should write `A TEST MESSAGE` to the display of your microbit. now see if you can work out how to change the message to something of your own and test it again to make sure that it works. 

## The plug board cipher

The job of a plug in the plugboard is simply to swap one character for another character (like a *find and replace* operation). You can make this microbit act either as one plug or multiple, but we will start with one...

Look in your code and find the `plug_from` and `plug_to` variables. `plug_from` is what character you want to *find*, and `plug_to` is the character that you want to *replace* it with, and vice versa. For example, in the template above, you have:

```python
# set the plugs (single characters)
plug_from = 'T'
plug_to   = 'F'
```

So if you encrypted the message:

```txt
FLIGHT SERGEANT
```

... then it would turn into:

```txt
TLIGHF SERGEANF
```

Can you see how that works? Each `T` has  become an `F` and each `F` has become a `T`. Simple!

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

`out` is a **variable** - this simply stores a value. In this case, we are storing a copy of the contents of `msg` into the `out` **variable** using the assigment operator (`=`).

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

## Making the plug

In our case, we want our `apply_encryption` **function** to take in one **argument** called `msg`, which contains our message to encrypt, apply our plugboard encryption, and then **return** the encrypted text. Your job is simply to fill in the code for the function to apply the encryption. Here is what we need it to do:

1. Make sure that we can access `plug_from` and `plug_to` 
2. Look at every character in turn
3. If it is the character in `plug_from`, switch it for the character in `plug_to`
4. If it is the character in `plug_to`, switch it for the character in `plug_from`
5. Otherwise, just keep the original character

Let's go...

### Step 1: Accessing the `plug_from` and `plug_to` variables

To make sure that you can access the `plug_from` and `plug_to` values (which are not inside the **function**), add this line to the top of your **function** (remember, things inside the function are **indented**)

```python
 global plug_from, plug_to
```

It should now look like this:

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
    global plug_from, plug_to
    
    out = msg
    return out
```

### Step 2: Looking at every character

Currently, our function is simply making a copying  `msg` into `out`, which gets returned, so it simply returns the same message that we started with. Clearly this is not what we want, so change this line:

```python
out = msg
```

To this:

```python
out = ""
```

This means that out is now an empty block of text. We can now add our encrypted characters to it one by one until we are finished.

In Python, we call a block of text a **String** of **characters** - Python cannot read, so it doesn't see words, simply lists of characters. To look through each element in a **list** in turn, we use a `for` **loop**, which is a bit of code that repeats once for each item in a **list**. Here is how it works:

```python
for char in msg:	
  out += char
```

As you can see, inside the `for` loop is another indented block - this runs once per **item** in the **list** (character in the message). Here, it is adding (`+=`) the current character (`char`) to the end of our new message - which will simply duplicate the original message.

Add the above to your code below `out = ""` but above `return out`, making sure that it is indented (the second line also needs to be indented a second time, to show that it is inside the `for` **loop**). 

Now run your code. If it works, it should still write the original message to the screen, but now it is doing it by adding each character one by one, rather than all at once. 

### Step 3: Swapping letters

The next step is to work out if each character is `plug_from` and if so, switch it for `plug_to`. We can do this with an `if` statement, which is a bit of code that tests whether or not somethign is true, and acts accordingly. For example:

```python
if char == plug_from:
    out += plug_to
else:
    out += char
```

This checks whether the current character (`char`) is equal to (`==`) the character stored in the `plug_from`  **variable**. If so, then it swaps it for the character stored in the `plug_to` **variable**. Otherwise (`else`), it simply adds the character as we were doing before.

Replace the contents of the `for` **loop** with the above code and then run it. If you have done it correctly, any `T` characters in your message should now appear as `F`. 

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

Now see if you can add an `elif` condition to the `if` statement to make it swap the letters in the *other* direction (i.e., from `plug_from` to `plug_to`). 

If all has gone to plan, when you run your code with the test message set to `FLIGHT SERGEANT`, you should get the same enciphered message as I did (`TLIGHF SERGEANF`).

## When you are finished

Once you are happy that your code works, you can simply delete the line that says `test()` (the last line), and add the following code to the bottom of your script:

```python
# turn on the radio interface
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
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()
```

This simply handles the radio communications between the microbits and makes a **call** to your `apply_encryption` **function** - feel free to take a look (see if you can find the function call), but don't worry if you don't fully understand it. 

Once that is done - your microbit is ready to be added to the rest of them to make the enigma machine!