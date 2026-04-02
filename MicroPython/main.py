"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *

# Initial setup
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        display.clear()

        # Turn on Red (P13=0, P14=1, P15=0)
        pin13.write_digital(0)
        pin14.write_digital(1)
        pin15.write_digital(0)
        display.scroll("Red")
        sleep(1000)

        # Turn on Blue (P13=1, P14=0, P15=0)
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(0)
        display.scroll("Blue")
        sleep(1000)

        # Turn on Green (P13=0, P14=0, P15=1)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Green")
        sleep(1000)

        # Turn on Magenta (P13=1, P14=1, P15=0)
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(0)
        display.scroll("Magenta")
        sleep(1000)

        # Turn on Yellow (P13=0, P14=1, P15=1)
        pin13.write_digital(0)
        pin14.write_digital(1)
        pin15.write_digital(1)
        display.scroll("Yellow")
        sleep(1000)

        # Turn on Cyan (P13=1, P14=0, P15=1)
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Cyan")
        sleep(1000)

        # Turn on White (P13=1, P14=1, P15=1)
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(1)
        display.scroll("White")
        sleep(1000)

        # Reset pins and show happy face again
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        display.show(Image.HAPPY)

    sleep(10)
