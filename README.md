# Lancaster Enigma Project

## Introduction

This repository contains code used by [345 (City of Lancaster) Squadron Air Cadets](https://lancasteraircadets.co.uk/) to create an Enigma machine out of a [Raspberry Pi](https://www.raspberrypi.org/) and several [BBC Microbits](https://www.bbc.co.uk/programmes/articles/4hVG2Br1W1LKCmw8nSm9WnQ/the-bbc-micro-bit) using [Python](https://www.python.org/). 

The project for the cadets was to build an Enigma simulator in which each major component of the Enigma device (plugboard, rotor, reflector) was represented by a separate BBC Microbit, with a Raspberry Pi used as the interface. The Microbits talk to each other via Radio, and to the Raspberry Pi using over USB. The code in the `Enigma_Components` directory is all you need to replicate this. The other sections comprise Enigma simulators that can be run either directly on any machine (`enigma.py`) or between a Raspberry Pi and a single BBC Microbit (`enigma_serial.py` and `micro_enigma.py` respectively); as well as simple demos for how to communicate over USB between a Raspberry Pi and BBC Microbit.

## Enigma Implementation

This implementation follows the description by Singh (2002). This is intended to be divided up into a series of BBC Microbits for the purpose of building a simple demonstration model of an Enigma machine - it is written with this in mind and to maximise simplicity and readability and to facilitate learning, rather than efficiency or programming best practice. In particular, it uses a very simple rotor model, which is randomly generated (in the simulators) or hard coded (in the components) and does not have a 'ring' setting.

In the reference implementation (`Enigma_Simulators/enigma.py` or `Enigma_Simulators/micro_enigma.py`), each submitted character goes through:
 - a plugboard (each wire on the plugboard will be one microbit)
 - three rotors (each rotor will be one microbit)
 - a reflector (one microbit)
 - the three rotors again
 - the plugboard again

After each character, the rotors move on one position, meaning that the same character in plain text will not be encrypted to the given the same character in cipher text. The rotors move:

 - rotor 1 moves every character
 - rotor 2 moves once every full revolution of rotor 1
 - rotor 3 moves once every full revolution of rotor 2

The initial settings of the machine (passed to init) are important, as a message can only be decrypted using the identical settings. These are the starting positions of the three rotors and a seed for the random number generator (which we use to generate the rotor wiring) - the latter could be hard-coded to eliminate this setting if preferred.

When the code in `Enigma_Components`is used to make the demo using BBC Microbits, any number of plugs and rotors can be included, which allows flexibility depending on the number of participants / Microbits you have available. If fewer than three BBC Microbits are available (allowing at least one of each component), then it might be better to use `pi_enigma.py` and `micro_enigma.py` code in the `Enigma_Simulators` directory instead (only one BBC Microbit required), or even use `enigma.py` (no BBC Microbits required).

## Repo Structure

This repo contains:

* **Enigma_Components** *(individual components that are used to build an Enigma Simulator using a Raspberry Pi and three or more BBC Microbits as described above)*
  * `input.py`: a simple interactive terminal to provide a keyboard and screen interface to the BBC Microbits (runs on Raspberry Pi).
  * `plug.py`: an implementation of a single pair of plugs on a plug board (runs on BBC Microbit).
  * `rotor.py`: an implementation of a simple rotor for which the wiring is randomly generated and there is no ring setting - see above (runs on BBC Microbit).
  * `reflector.py`: an implementation of a simple reflector for which the wiring is randomly generated  (runs on BBC Microbit).
* **Enigma_Simulators** *(Enigma Simulators that can be run directly on a Raspberry Pi alone, or with one BBC Microbit)*
  * `enigma.py`: a pure Python 3 implementation of a simple enigma simulator, complete with interactive terminal. This code can be used on any computer with Python 3 installed (Windows, Linux, Mac), but not on a BBC Microbit.
  * `micro_enigma.py`: an implementation of the simple enigma simulator that can be run on a BBC Microbit. The input and output is via USB, which can be achieved using `pi_enigma.py`.
  * `pi_enigma.py`: an interactive terminal for use on a Raspberry Pi to interact with `micro_enigma.py`.
* **Communication_ Demos** *(A simple demo of how to communicate between a Raspberry Pi and BBC Microbit)*
  * `micro_serial_rw.py`: an extremely simple implementation of reading and writing to USB for a BBC Microbit. Can be used with `serial_rw.py` for demonstration purposes.
  * `pi_serial_rw.py`: an extremely simple implementation of reading and writing to USB for a Raspberry Pi. Can be used with `microbit_serial_rw.py` for demonstration purposes.
  * `micro_radio.py`: a simple demo of how to communicate between BBC Microbits using the built in radio interface.