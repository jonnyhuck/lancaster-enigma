# Lancaster Enigma Project

## Introduction

This repository contains code used by [345 (City of Lancaster) Squadron Air Cadets](https://lancasteraircadets.co.uk/) to create an Enigma machine out of a [Raspberry Pi](https://www.raspberrypi.org/) and several [BBC Microbits](https://www.bbc.co.uk/programmes/articles/4hVG2Br1W1LKCmw8nSm9WnQ/the-bbc-micro-bit) using [Python](https://www.python.org/). 

The project for the cadets was to build an Enigma simulator in which each major component of the Enigma device (plugboard, rotor, reflector) was represented by a separate BBC Microbit, with a Raspberry Pi used as the interface. The Microbits talk to each other via Radio, and to the Raspberry Pi using over USB. The code in the `Enigma Components` directory is all you need to replicate this. The other sections comprise Enigma simulators that are 

## Enigma Implementation

This implementation follows the description by Singh (2002). This is intended to be divided up into a series 
of BBC Microbits for the purpose of building a simple demonstration model of an Enigma machine - it is written with this in mind and to maximise simplicity and readability, rather than efficiency or progrramming best practice. In particular, it uses a very simple rotor model, which is randomly generated and does not have a 'ring' setting.

In the reference implementation (`Simulators/enigma.py` or `Simulators/microbit_enigma.py`), each submitted character goes through:
 - a plugboard (each wire on the plugboard will be one microbit)
 - three rotors (each rotor will be one microbit)
 - a reflector (one microbit)
 - the three rotors again
 - the plugboard again

After each character, the rotors move on one position, meaning that the same character in plain text will not be encrypted to the given the same character in cipher text. The rotors move:

 - rotor 1 moves every character
 - rotor 2 moves once every full revolution of rotor 1
 - rotor 3 moves once every full revolution of rotor 2

The initial settings of the machine (passed to init) are important, as a message can only be decrypted using the
    identical settings. These are the starting positions of the three rotors and a seed for the random number generator 
    (which we use to generate the rotor wiring) - the latter could be hard-coded to eliminate this setting if preferred.

## Repo Structure

This repo contains:

* **Enigma_Components** *(the code used in our project to create the )*
  * 
* **Simulators** *(Enigma Simulators in a single file)*
  * `enigma.py`: a pure Python 3 implementation of a simple enigma simulator, complete with interactive terminal. This code can be used on a machine with any OS, but not on a BBC Microbit.
  * `microbit_enigma.py`: an implementation of the whole enigma simulator from `enigma.py`that can be run on a BBC Microbit. The input and output is via USB.
* **Communication_ Demos** *(Useful demos of how to communicate between a Raspberry Pi and BBC Microbit)*
  * `microbit_serial_rw.py`: an extremely simple implementation of reading and writing to USB for a BBC Microbit. Can be used with `serial_rw.py` for demonstration purposes.
  * `serial_rw.py`: an extremely simple implementation of reading and writing to USB for a Raspberry Pi. Can be used with `microbit_serial_rw.py` for demonstration purposes.