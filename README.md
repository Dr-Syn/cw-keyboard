# cw-keyboard
This is a small set of python programs for the pyboard 1.0 that allows you to use a telegraph key to enter morse code, translating it into keyboard events

## Installation

Copy all the files into the data directory of a pyboard 1.0

This -may- work on other pyboards but I do not have any examples to test with.

Hit the rst key and short the X2 pin to GND [ e.g. by hooking those up to a telegraph key ]

The green LED should come on to indicate a successful contact. When a valid morse code sequence is entered, an HID event will be generated to output that character to the computer the pyboard is attached to.

## Configuration and Customization

lookups.py holds the translation. Please note the use of the AA prosign to indicate the return key and the AS prosign for a space. 

Also, '--.-.-' has been assigned to a 'shift' indicator. This should act as per a shift key on the keyboard - e.g. shift + a = A and shift + 1 = !

Some characters on the keyboard are missing; if you wand them, add them to the kbmap in lookups.py by their scan codes, and add some means of invoking them into the morse dict.

Certain delays are built into the main.py routine.

In the main loop, there is a delay of 200ms to allow you to enter the next dot or dash.
getpin has a loop calibrated to a minimum 200ms key-down to register; < 400 ms for a dot; and 600ms threshold for a dash.
There is also a rekey delay if you hold down for longer than 600ms because you probably need it if you're being that slow.

Good luck!
