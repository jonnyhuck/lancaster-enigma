# # Making a Rotor

First, open the MicroBit Python editor by clicking [here](https://python.microbit.org/v/3), clear all of the code that is in there and and paste in the below code instead - this is a template to get you started:

```python
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
THESE ARE JUST SOME SETTINGS THAT THE CODE REQUIRES FOR OPERATION

`my_id` SETS THE POSITION OF THIS COMPONENT IN THE ENIGMA MACHINE. YOU DON'T 
NEED TO WORRY ABOUT THIS UNTIL WE JOIN THE MACHINE TOGETHER.
'''

# the id of this device - should denote the devices position in the Enigma
my_id = 4

# this simply defines the alphabet, it is needed for the operation of the rotor
alphabet  = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


'''
THIS JUST CALLS THE TEST FUNCTION SO THAT YOU CAN TEST YOUR ENCRYPTION CODE - YOU WILL
REMOVE THIS LATER
'''
test()

```

Run this code, it should write `A TEST MESSAGE` to the display of your microbit. now see if you can work out how to change the message to something of your own and test it again to make sure that it works. 

## The rotor cipher

The job of a rotor is simply to scramble the alphabet. Every character is wired to another character, which is used as a replacement for the original. Every time a letter moves through the machine, the wiring in the rotor rotates one step, meaning that the character is now wired to a different character. This means that the same character is converted to a different character each time it is used, making it harder to break the cipher.

This wiring is represented in your code by two **lists** of characters, one of which is the normal alphabet, and one of which is a scrambled version. First, find where we identify `alphabet` in your code. Once you can see where that is, take a look at the code below- this is where the two lists get defined (this is already in your code, you don't need to copy and paste it).

```python
def build_rotor():
    """
    THIS FUNCTION SETS (OR RESETS) THE ROTORS TO THEIR ORIGINAL POSITION - YOU CAN CHANGE THE `r_to` LIST
    BELOW TO CHANGE THE WIRING OF THE ROTOR - JUST MAKE SURE THAT EACH LETTER IS ONLY IN THERE ONCE!
    """
    r_from  = alphabet.copy()
    r_to = ['K', 'W', 'C', 'S', 'J', 'F', 'R', 'V', 'L', 'E', 'N', 'P', 'I', 
            'O', 'Y', 'M', 'D', 'U', 'A', 'T', 'Z', 'B', 'H', 'X', 'G', 'Q']
    return [r_from, r_to]
```

Your job when vcreating the encryption is therefore firstly to swap each latter in `r_from` (`alphabet`) for its counterpart in the `r_to`. 

One interesting thing about rotors is that they have to work in both directions, so you need to know whether or not you are enciphering the message forwards or backwards. Like the plug board, a message will pass through each rotor twice, one before the reflector, and once after.

The other thing is that the letters in `r_to` change after each character passes through the machine. For this reason, enciphering the same letter twice will result in a different result each time!

## Some coding basics

To implement this encryption in Python, you need to edit the `def apply_encryption(msg):` **function**. A **function** is simply a block of code that does something, and is created using a `def` (define) statement, after everything inside the function should be **indented** underneath the `def` statement. You can see this in the function as it is at the moment:

```python
def apply_encryption(msg, forward):
    """
    THIS FUNCTION NEEDS TO ENCRYPT THE MESSAGE BY FINDING ANY CHARACTERS IN `rotor_from` 
    AND SWAPPING THEM WITH THE CORRESPONDING CHARACTER IN `rotor_to` (WHEN `forward` == `True`)
    AND VICE VERSA (when `forward` == `False`).

    TO BE ABLE TO WORK IN BOTH DIRECTIONS, YOU WILL NEED TO 'ADVANCE' THE ROTOR BETWEEN EACH CHARACTER.
    """
    out = msg
    return out
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

## Making the rotor

In our case, we want our `apply_encryption` **function** to take in one **argument** called `msg`, which contains our message to encrypt, apply our plugboard encryption, and then **return** the encrypted text. Your job is simply to fill in the code for the **function** to apply the encryption. Here is what we need it to do:

1. Look at every character in turn
2. Advance the rotor
3. If the character is in  `r_from`, get its position in the **list** and replace it with the corresponding character in `r_to` (vice versa if `forward == False`)
4. Otherwise, just keep the original character

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

If, rather than access each item in the **list** individually, we would like to systematically look through each element in turn, we use a `for` **loop**, which is a bit of code that repeats once for each item in a **list**. Here is how it works:

```python
for count, char in enumerate("Hi mum!"):	
  print(count, char)
```

As you can see, inside the `for` loop is another indented block - this runs once per **item** in the **list** (character in the message in our case). Note that we are also using the `enumerate` function here. This numbers each of the characters (starting at `0`), so we get a number in the `count` variable, and the character in the `char` variable. The above loop, for example, would print out this:

```
0 H
1 i
2  
3 M
4 u
5 m
```

In our case, we don't want to print out the lists of numbers, we want to assemble them back into a message (which eventually will be encrypted). To do this, add this loop to your `apply_encryption` function.

```python
for count, char in enumerate(msg):	
  out += char
```

Here, it is adding (`+=`) the current character (`char`) to the end of our new message - which will simply  duplicate the original message.

Add the above to your code below `out = ""` but above `return out`, making sure that it is indented (the second line also needs to be indented a second time, to show that it is inside the `for` **loop**). 

Now run your code. If it works, it should still write the original message to the screen, but now it is doing it by adding each character one by one, rather than all at once. 

### Step 2: Advancing the rotor

Rotor advancement in a mechanical Enigma machine is relatively straightforward machine - basically, the jumble of wires rotates forwards while the letters remain in the same place, meaning that each letter is mapped to a different one after every iteration. In code, however, it is a little complex, so I have provided the necessary 

Now, add this function to your code, just above the `build_rotor` function. Remember that the `def` statement should not be indented, and the contents of the function should be indented as shown below:

```python
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
```

Then, add the following three lines to your `for` loop in the `apply_encryption` **function**. These should be the first three lines in your loop.

The next step depends on what rotor you are building - find the correct snippet below and add them to the **top** of your `apply_encryption` function (just below the **comment**).

#### Rotor 1 should add this:

```python
        # get the character number for this message
        n = count + 1

        # put the rotor back to the start
        rotor = build_rotor()

        # advance the rotor the correct number of positions
        rotor = advance_rotor(rotor, n)
```

#### Rotor 2 should add this:

```python
        # get the character number for this message
        n = count + 1

        # put the rotor back to the start
        rotor = build_rotor()

        # advance the rotor the correct number of positions (once per revolution of rotor 1)
        if n % len(alphabet) == 0:
            rotor = advance_rotor(rotor, n // len(alphabet))
```

#### Rotor 3 should add this:

```python
        # get the character number for this message
        n = count + 1

        # put the rotor back to the start
        rotor = build_rotor()

        # advance the rotor the correct number of positions (once per revolution of rotor 2)
        if n % (len(alphabet)**2) == 0:
            rotor = advance_rotor(rotor, n // (len(alphabet)**2))
```

This will act to reset your rotor then advance it the correct number of times for the current character - meaning that it will always end up in the right place! Note how we are adding 1 to the `count` value each time - this gives the effect of counting from `1` upwards instead of from `0` upwards - which is what we need!

### Step 3: Swapping letters and searching lists

The next step is to work out if each character is in `r_from` and if so, switch it for the corresponding letter in  `r_to`. We can do this with an `if` statement, which is a bit of code that tests whether or not something is true, and acts accordingly. For example:

```python
# which direction?
if forward:

  # run through the reflector (r1->r2)
  if char in r_from:
      out += r_to[r_from.index(char)]

  # we are only encrypting letters at the moment - anything else goes straight back
  else:
      out += char
```

The first line in the above snippet checks whether the `forward` **argument** is set to `True`. The second then checks whether the current character (`char`) is in the **list** `r_from`. 

If so, we need to work out what position in the list it is (remember, the first item in the list is position `0`, the second is position `1`, and so on). We can do this with `r_from.index(char)`, which is a **function** that **returns** the position (**index** number) of `char` in `r_from`. We then pass that to `r_to` using square brackets `[ ]` to retrieve the that is in this position. Finally, we append the character from `r_to` to `out` (`+=`) instead of the original character, thus encrypting it.

Replace the contents of the `for` **loop** with the above code and then run it. If you have done it correctly, the letters from `r1`should all be replaced with their counterparts from `r2`.

If all has gone to plan, when you run your code the characters should all be completely scrambled

### Step 4: working in reverse

The above step works for when the signal is coming forward through the Enigma machine (before it hits the reflector). After that the rotor has to work the opposite way around (i.e., from `r_to` to `r_from`). 

Add an `else` clause to the `if forward:` statement and add in the necessary code to handle the rotor in the opposite direction (*Hint:* you just need the same code, but with `r_from` and `r_to` swapped over...).

## When you are finished

Once you are happy that your code works, you can simply delete the line that says `test()` (the last line), and add the following code to the bottom of your script:

```python
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
            encrypted = apply_encryption(msg_components[2].upper(), forward)
            
            # work out next destination
            destination = my_id + 1 if forward else my_id - 1

            # pass on the message
            radio.send("|".join([str(destination), str(forward), encrypted, msg_components[3]]))
            display.clear()
```

This simply handles the radio communications between the microbits and makes a **call** to your `apply_encryption` **function** - feel free to take a look (see if you can find the function call), but don't worry if you don't fully understand it. 

Once that is done - your microbit is ready to be added to the rest of them to make the Enigma machine!